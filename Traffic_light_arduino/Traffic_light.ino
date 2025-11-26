// -------------------------------------------------------
// Simple Traffic Light - Procedural Example for Students
// -------------------------------------------------------
// Demonstrates:
// - constants and variables
// - functions (procedures)
// - step-by-step control flow
// - using delays for timing
// -------------------------------------------------------

// ----- Pin assignments -----
const int RED_LED_PIN    = 2;
const int YELLOW_LED_PIN = 3;
const int GREEN_LED_PIN  = 4;

// ----- Timing (in milliseconds) -----
const unsigned long GREEN_TIME  = 4000; // 4 seconds
const unsigned long YELLOW_TIME = 1000; // 1 second
const unsigned long RED_TIME    = 4000; // 4 seconds

// -------------------------------------------------------
// setup: runs once at the beginning
// -------------------------------------------------------
void setup() {
  pinMode(RED_LED_PIN, OUTPUT);
  pinMode(YELLOW_LED_PIN, OUTPUT);
  pinMode(GREEN_LED_PIN, OUTPUT);

  // Start with all lights off
  allLightsOff();
}

// -------------------------------------------------------
// loop: runs over and over
// -------------------------------------------------------
void loop() {
  // The whole program is just a clear sequence of procedures:
  runGreenPhase();
  runYellowPhase();
  runRedPhase();
}

// -------------------------------------------------------
// Helper: turn all LEDs off
// -------------------------------------------------------
void allLightsOff() {
  digitalWrite(RED_LED_PIN, LOW);
  digitalWrite(YELLOW_LED_PIN, LOW);
  digitalWrite(GREEN_LED_PIN, LOW);
}

// -------------------------------------------------------
// Helper: set exactly one light on (like a real traffic light)
// -------------------------------------------------------
void showOnlyRed() {
  allLightsOff();
  digitalWrite(RED_LED_PIN, HIGH);
}

void showOnlyYellow() {
  allLightsOff();
  digitalWrite(YELLOW_LED_PIN, HIGH);
}

void showOnlyGreen() {
  allLightsOff();
  digitalWrite(GREEN_LED_PIN, HIGH);
}

// -------------------------------------------------------
// Phase procedures
// Each phase is a clear, self-contained procedure.
// -------------------------------------------------------
void runGreenPhase() {
  showOnlyGreen();          // 1) turn on green
  delay(GREEN_TIME);        // 2) wait
}

void runYellowPhase() {
  showOnlyYellow();         // 1) turn on yellow
  delay(YELLOW_TIME);       // 2) wait
}

void runRedPhase() {
  showOnlyRed();            // 1) turn on red
  delay(RED_TIME);          // 2) wait
}
