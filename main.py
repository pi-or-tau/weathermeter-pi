import assigner
import sun_time


sun = sun_time.sun()
current = assigner.vari_init()

print('Temperature: ' + str(current.temp_F) + 'F')
print('Weather: ' + current.weather_description)
print('Sunrise: ' + current.sunrise)
print('Sunset: ' + current.sunset)
print('At: ' + current.time_taken)

#print(sun.text2int(current.sunset[0]))
