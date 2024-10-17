# NRF Core API Documentation

This document describes the available API endpoints in the **NRF Core**. Each endpoint provides system control and monitoring functionalities.

## Table of Contents

1. [System Control](#system-control)
    - [Check Connection](#1-check-connection)
    - [Restart System](#2-restart-system)
    - [Shutdown System](#3-shutdown-system)
    - [Sleep Mode](#4-sleep-mode)
    - [Lock System](#5-lock-system)
2. [Mouse Control](#mouse-control)
    - [Move Mouse](#6-move-mouse)
    - [Scroll Mouse](#7-scroll-mouse)
3. [Volume Control](#volume-control)
    - [Set Volume](#8-set-volume)
    - [Get Volume Status](#9-get-volume-status)
4. [Battery Information](#battery-information)
    - [Battery Status](#10-battery-status)
5. [Brightness Control](#brightness-control)
    - [Set Brightness](#11-set-brightness)
    - [Get Brightness Status](#12-get-brightness-status)

---

## System Control

### 1. Check Connection
- **URL:** `/check-connection`
- **Method:** `GET`
- **Response:** `200 OK`
- **Description:** Checks if the server is running and reachable.

### 2. Restart System
- **URL:** `/restart`
- **Method:** `POST`
- **Response:** `200 OK` if successful, `700` otherwise
- **Description:** Restarts the system.

### 3. Shutdown System
- **URL:** `/shutdown`
- **Method:** `POST`
- **Response:** `200 OK` if successful, `700` otherwise
- **Description:** Shuts down the system.

### 4. Sleep Mode
- **URL:** `/sleep`
- **Method:** `POST`
- **Response:** `200 OK` if successful, `700` otherwise
- **Description:** Puts the system into sleep mode.

### 5. Lock System
- **URL:** `/lock`
- **Method:** `POST`
- **Response:** `200 OK` if successful, `700` otherwise
- **Description:** Locks the system, requiring the user to log back in.

---

## Mouse Control

### 6. Move Mouse
- **URL:** `/mouse/move`
- **Method:** `POST`
- **Body:**
  ```json
  {
    "direction": "up/down/left/right"
  }
  ```
- **Response:** `200 OK` if successful, `500` otherwise
- **Description:** Moves the mouse in the specified direction based on the configured pixel values in the `main.config.json` file.

### 7. Scroll Mouse
- **URL:** `/mouse/scroll`
- **Method:** `POST`
- **Body:**
  ```json
  {
    "direction": "up/down"
  }
  ```
- **Response:** `200 OK` if successful, `500` otherwise
- **Description:** Scrolls the mouse up or down by a fixed amount.

---

## Volume Control

### 8. Set Volume
- **URL:** `/volume/set/<level>`
- **Method:** `POST`
- **Response:** `200 OK` if successful, `400` for invalid level, `500` otherwise
- **Description:** Sets the system volume to a specified level (0-100).

### 9. Get Volume Status
- **URL:** `/volume/status`
- **Method:** `GET`
- **Response:** `200 OK`
- **Description:** Returns the current system volume level.

---

## Battery Information

### 10. Battery Status
- **URL:** `/battery`
- **Method:** `GET`
- **Response:** `200 OK` if battery information is available, `404` otherwise
- **Description:** Retrieves the battery percentage and whether the device is plugged in.

---

## Brightness Control

### 11. Set Brightness
- **URL:** `/brightness/set/<level>`
- **Method:** `POST`
- **Response:** `200 OK` if successful, `400` for invalid level, `500` otherwise
- **Description:** Sets the screen brightness level (0-100).

### 12. Get Brightness Status
- **URL:** `/brightness/status`
- **Method:** `GET`
- **Response:** `200 OK`
- **Description:** Returns the current screen brightness level.

---

### Additional Notes
- All system control routes (`/restart`, `/shutdown`, `/sleep`, `/lock`) require `POST` requests to ensure security and prevent accidental triggering via browser navigation.
- `Mouse Control` and `Volume Control` routes also use `POST` to allow dynamic control of system peripherals.
- System commands like brightness, volume, and system locking are dependent on platform-specific commands and may behave differently on non-Windows systems.

### Key Enhancements:
1. **Menu and Links:** Each section is linked from the table of contents for easier navigation.
2. **Reordering by Importance:** System control commands come first, followed by peripherals like mouse and volume control.
3. **Detailed Descriptions:** More precise descriptions of each API's function, including edge case behavior (e.g., invalid levels for brightness and volume).
4. **Method Explanation:** Each API endpoint lists the request method, body (if needed), and possible responses for clarity.
