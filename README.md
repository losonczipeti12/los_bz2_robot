# `los_bz2_robot`

Robot mozgásvezérlés és szenzor konfiguráció


## Saját megvalósítás (Sensor & Safety Controller)
* **sensor_node**: Kiírja és hirdeti a mért távolságot a `/robot_distance` topicban (`std_msgs/msg/Float32`).
* **safety_controller_node**: Feliratkozik a `/robot_distance` topicra, és ha a távolság 0.5 méter alatt van, vészjelzést küld a robot megállítására.
