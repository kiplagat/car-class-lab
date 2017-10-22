class Car(object):
	def __init__(self, name="General",model="GM",type_="saloon",):
		self.type_ = type_
		self.name = name
		self.num_of_wheels = 4
		self.model = model
		self.num_of_doors = 4
		self.speed = 0


		if self.name == "Porshe" or self.name == "Koenigsegg":
			self.num_of_doors = 2
		if self.type_ == "trailer":
			self.num_of_wheels = 8
	def is_saloon(self):
		if self.type_ == "saloon":
			return True
		else:
			return False

	def drive(self,pedal_press=0):
		self.pedal_press = pedal_press
		if self.pedal_press == 3:
			self.speed = 1000
			return self
		if self.pedal_press == 7:
			self.speed = 77
			return self
		