# smart-maintenance-qr
Industrial maintenance management system using QR codes


# Smart Maintenance QR

Sistema de digitalización de mantenimiento industrial mediante códigos QR por máquina.

## Problema que resuelve

En muchas plantas industriales, la información de cada máquina (manual, historial de averías, repuestos y su ubicación) está dispersa y es de difícil acceso para el personal de mantenimiento. Además, el registro de cambio de turno suele hacerse de forma manual en papel, duplicando el trabajo ya registrado por máquina.

## Solución

Cada máquina de la planta tiene un código QR único. Al escanearlo, el personal de mantenimiento accede a:

- Ficha técnica y manual de la máquina.
- Historial de eventos (averías, mantenimientos, comentarios).
- Repuestos compatibles y su ubicación exacta en almacén.
- Analítica básica de paradas y averías.

El cuaderno de cambio de turno se genera automáticamente a partir de los eventos registrados en cada máquina, eliminando el registro manual duplicado.

## Estado del proyecto

🚧 En desarrollo.

## Stack técnico

- Backend: Python (FastAPI)
- Base de datos: PostgreSQL
- Frontend: HTML + Bootstrap
- Generación de QR: librería `qrcode`