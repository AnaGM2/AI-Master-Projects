/* -------------------- */
/* F U Z Z Y    S E T S */
/* -------------------- */

// Sets for ToF sensor range [0 .. 10] (meters)
set CLOSE	= trapezoid {0.0, 0.0, 0.2, 0.3};			// Close 
set NEAR	= trapezoid {0.2, 0.3, 0.4, 0.5};			// Near 
set MED		= trapezoid {0.4, 0.5, 0.6, 0.7};			// Medium
set FAR		= trapezoid {0.6, 0.7, 1.3, 1.4};			// Far
set VFAR	= trapezoid {1.3, 1.4, 10.0, 10.0};			// Very Far

// Sets for steering [-180 .. 180]
set TTR		= trapezoid {-150.0, -150.0, -100.0, -90.0};	// Tight Right
set TR		= trapezoid {-100.0, -90.0, -60.0, -50.0};		// Right
set TSR		= trapezoid {-60.0, -50.0, -20.0, -10.0};		// Small Right
set TC		= trapezoid {-20.0, -10.0, 10.0, 20.0};			// Center
set TSL		= trapezoid {10.0, 20.0, 50.0, 60.0};			// Small Left
set TL		= trapezoid {50.0, 60.0, 90.0, 100.0};			// Left
set TTL		= trapezoid {90.0, 100.0, 150.0, 150.0};		// Tight Left

// Sets for speed [0 .. 1] (percentage)
set SFULL	= trapezoid {0.25, 0.3, 0.5, 0.5};				// Full speed
set SMEDIUM	= trapezoid {0.15, 0.2, 0.25, 0.3};				// Medium speed
set SLOW	= trapezoid {0.0, 0.0, 0.15, 0.2};				// Stop

// Sets for blending [0 ..1 ] 
set LOW		= trapezoid {0.0, 0.0, 0.1, 0.2};			// Low
set HALFL	= trapezoid {0.1, 0.2, 0.4, 0.5};			// Medium
set HALFH	= trapezoid {0.4, 0.5, 0.7, 0.8};			// Medium
set HIGH	= trapezoid {0.7, 0.8, 1.0, 1.0};			// High

/* ----------------- */
/* C O N S T A N T S */
/* ----------------- */


/* ----------------- */
/* V A R I A B L E S */
/* ----------------- */

// External Blackboard Variables
sensor float		group0, group1, group2, group3, group4;
sensor float 		bumper0, bumper1, bumper2, bumper3;
sensor float 		alpha, heading;
effector float 		turn, speed;

// State and Control Variables
float 				collision = 0.0;
float 				left, leftd, front, rightd, right; 	// Group sensors

/* ----------------- */
/* F U N C T I O N S */
/* ----------------- */

function min (a, b)
{
	if (a < b) return a;
	return b;
}

function max (a, b)
{
	if (a > b) return a;
	return b;
}

function limits (x, a, b)
{
	if (x < a) return a;
	if (x > b) return b;
	return x;
}

function sgn (a)
{
	if (a < 0.0) return -1.0;
	if (a > 0.0) return 1.0;
	return 0.0;
}


/* --------------------------- */
/* I N I T I A L I Z A T I O N */
/* --------------------------- */

initialization
{
	turn = 0.0;
	speed = 0.0;
}


/* ----------- */
/* A G E N T S */
/* ----------- */

agent ReactiveControl
{
	blending	left range (0.0, 2.0), leftd range (0.0, 1.0), right range (0.0, 2.0), rightd range (0.0, 1.0), front range (0.0, 2.0), collision range (0.0, 1.0);

	common
	{
		left	= group0;
		leftd	= group1;
		front	= group2;
		rightd	= group3;
		right	= group4;
		
		collision = bumper0 + bumper1 + bumper2 + bumper3;
		if (collision > 1.0) collision = 1.0;
	}

	behaviour followLeftWall priority 1.0
	{
	    fusion turn, speed;
	
	    rules
	    {
	        background (0.01) speed is SFULL;
	        background (0.01) turn is TC;
	
	        // Mantener distancia con la pared izquierda
	        if (leftd is CLOSE)                     turn is TR;
	        if (leftd is NEAR)                      turn is TSR;
	        if (leftd is MED)                       turn is TC;
	
	        // Manejar esquinas y giros cerrados
	        if ((front is CLOSE) && (leftd is FAR)) turn is TR;
	        if ((front is CLOSE) && (leftd is CLOSE)) turn is TR;
	
	        // Reducir velocidad en esquinas
	        if ((front is CLOSE) || (leftd is CLOSE)) speed is SLOW;
	    }
	}

	behaviour recoverLeftWall priority 1.0
	{
	    fusion turn, speed;
	
	    rules
	    {
	        background (0.01) speed is SLOW;
	        background (0.01) turn is TSR; 
	
			// Gira a la izquierda para buscar la pared
	        if (leftd is FAR)                       turn is TSL;
	        if (leftd is VFAR)                      turn is TL;
	        
	        // Reducir velocidad y recolocar cerca de la pared
	        if (front is CLOSE) 					turn is TSR, speed is SLOW;
	    }
	}

	blender
	{
		// Reglas del blender
		rules
		{
			// Valores predeterminados
 			background (0.01) 					followLeftWall is LOW;
        	background (0.01) 					recoverLeftWall is LOW;

			// Mantener la pared izquierda
			if (leftd is CLOSE)					followLeftWall is HALFH;
        	if (leftd is NEAR)                  followLeftWall is HIGH;
        	if (leftd is MED)                   followLeftWall is HALFL;
        	
        	// Recuperar la pared izquierda
        	if (leftd is FAR)  					recoverLeftWall is HIGH;
        	if (leftd is VFAR)					recoverLeftWall is HIGH;
        	
		}
	}
}
