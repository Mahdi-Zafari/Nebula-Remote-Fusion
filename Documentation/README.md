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
    - [Mouse Click](#7-mouse-click)
    - [Scroll Mouse](#8-scroll-mouse)
3. [Volume Control](#volume-control)
    - [Set Volume](#9-set-volume)
    - [Get Volume Status](#10-get-volume-status)
4. [Battery Information](#battery-information)
    - [Battery Status](#11-battery-status)
5. [Brightness Control](#brightness-control)
    - [Set Brightness](#12-set-brightness)
    - [Get Brightness Status](#13-get-brightness-status)

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
- **URL:** `/mouse/move/<direction>`
- **Method:** `POST`
- **Parameters:**
  - `<direction>`: `up`, `down`, `left`, `right`
- **Response:** `200 OK` if successful, `500` otherwise
- **Description:** Moves the mouse in the specified direction by a configured amount in pixels.
  
  - **Endpoints**:
    - `/mouse/move/up`
    - `/mouse/move/down`
    - `/mouse/move/left`
    - `/mouse/move/right`
  
  - **Example Response**:
    ```json
    {
      "status": "mouse moved up"
    }
    ```

### 7. Mouse Click
- **URL:** `/mouse/click/<button>`
- **Method:** `POST`
- **Parameters:**
  - `<button>`: `left`, `right`
- **Response:** `200 OK` if successful, `500` otherwise
- **Description:** Clicks the specified mouse button (`left` or `right`).
  
  - **Endpoints**:
    - `/mouse/click/left`
    - `/mouse/click/right`
  
  - **Example Response**:
    ```json
    {
      "status": "left mouse click"
    }
    ```

### 8. Scroll Mouse
- **URL:** `/mouse/scroll/<direction>`
- **Method:** `POST`
- **Parameters:**
  - `<direction>`: `up`, `down`
- **Response:** `200 OK` if successful, `500` otherwise
- **Description:** Scrolls the mouse up or down by a fixed amount.
  
  - **Endpoints**:
    - `/mouse/scroll/up`
    - `/mouse/scroll/down`
  
  - **Example Response**:
    ```json
    {
      "status": "scrolled up"
    }
    ```

---

## Volume Control

### 9. Set Volume
- **URL:** `/volume/set/<level>`
- **Method:** `POST`
- **Response:** `200 OK` if successful, `400` for invalid level, `500` otherwise
- **Description:** Sets the system volume to a specified level (0-100).

### 10. Get Volume Status
- **URL:** `/volume/status`
- **Method:** `GET`
- **Response:** `200 OK`
- **Description:** Returns the current system volume level.

---

## Battery Information

### 11. Battery Status
- **URL:** `/battery`
- **Method:** `GET`
- **Response:** `200 OK` if battery information is available, `404` otherwise
- **Description:** Retrieves the battery percentage and whether the device is plugged in.

---

## Brightness Control

### 12. Set Brightness
- **URL:** `/brightness/set/<level>`
- **Method:** `POST`
- **Response:** `200 OK` if successful, `400` for invalid level, `500` otherwise
- **Description:** Sets the screen brightness level (0-100).

### 13. Get Brightness Status
- **URL:** `/brightness/status`
- **Method:** `GET`
- **Response:** `200 OK`
- **Description:** Returns the current screen brightness level.
