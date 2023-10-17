class VehData:

    def __init__(self):
        self.feature = 0
        self.incar_temperature = 0
        self.head_at_suitable_position = True
        self.setting_page_exit_time = False
        self.noise_level = 0
        self.passangers_on_phone = False
        self.off_road = False # off road or not
        self.location = False # near by shopping mall
        self.imu = 0
        self.battery_life = 0
        self.traffic_light = 0 # 0,1,2,3 None, red, green, yellow
        self.veh_inFrontOf = False
        self.eye_on_road = False
        self.veh_speed = 0
        self.driver_fatigue = False
        self.eye_on_shopping_mall = False

    def setData(self, feature, incar_temperature, head_at_suitable_position, setting_page_exit_time, noise_level, passangers_on_phone, off_road, location, imu, battery_life, traffic_light, veh_inFrontOf, eye_on_road, veh_speed, driver_fatigue, eye_on_shopping_mall):
        self.incar_temperature = incar_temperature
        self.head_at_suitable_position = head_at_suitable_position
        self.setting_page_exit_time = setting_page_exit_time
        self.noise_level = noise_level
        self.passangers_on_phone = passangers_on_phone
        self.off_road = off_road
        self.location = location
        self.imu = imu
        self.battery_life = battery_life
        self.traffic_light = traffic_light
        self.veh_inFrontOf = veh_inFrontOf
        self.eye_on_road = eye_on_road
        self.veh_speed = veh_speed
        self.driver_fatigue = driver_fatigue
        self.eye_on_shopping_mall = eye_on_shopping_mall
        self.feature = feature

    def strData(self):
        data = ("incar_temperature: " + str(self.incar_temperature) + "\n" + "head_at_suitable_position: " + str(self.head_at_suitable_position) + "\n" + "setting_page_exit_time: " + str(self.setting_page_exit_time) + "\n"
               + "noise_level: " + str(self.noise_level) + "\n" + "passangers_on_phone: " + str(self.passangers_on_phone) + "\n" + "off_road: " + str(self.off_road) + "\n"
               + "location: " + str(self.location) + "\n" + "imu: " + str(self.imu) + "\n" + "battery_life: " + str(self.battery_life) + "\n"
               + "traffic_light: " + str(self.traffic_light) + "\n" + "veh_inFrontOf: " + str(self.veh_inFrontOf) + "\n" + "eye_on_road: " + str(self.eye_on_road) + "\n"
               + "veh_speed: " + str(self.veh_speed) + "\n" + "driver_fatigue: " + str(self.driver_fatigue) + "\n" + "eye_on_shopping_mall: " + str(self.eye_on_shopping_mall) + "\n")
        return data