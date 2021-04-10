rgb = input("Enter an RGB value: ")
rgb = rgb.split(",")
rgb[0] = rgb[0][1:len(rgb[0])]
rgb[2] = rgb[2][0:(len(rgb[2])-1)]
for i in range(len(rgb)):
    rgb[i] = int(rgb[i])
rgbMax = max(rgb)
pwm = [0,0,0]
for i in range(len(rgb)):
    pwm[i] = str(rgb[i]/rgbMax)
print("("+pwm[0]+pwm[1]+pwm[2]+")")
