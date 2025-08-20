a=-0.2
b=1.5
c=24

def quadratic_weather_model(time):
    return a*(time**2)+b*time+c

#------Waterfall Model------------

print("---Waterfall Model---")
for hour in range(0,25,6):
    temp=quadratic_weather_model(hour)
    print(f"Time: {hour} hrs-> Predicted Temp: {temp:.2f}degree celsius")

#------Iterative Model------------

print("\n---Iterative Model---")
for iteration in range(1,4):
    print(f"Iteration {iteration}:")
    for hour in range(0,25,12):
        temp=quadratic_weather_model(hour)
        print(f"Time: {hour} hrs-> Predicted Temp: {temp:.2f}degree celsius")
    print("-----")

#-----------Agile Model------------

print("\n---Agile Model---")
times_to_check=[0,6,12,18,24]
for sprint in range(1,3):
    print(f"Sprint {sprint}:")
    for t in times_to_check:
        temp=quadratic_weather_model(t)
        print(f"Time: {t} hrs-> Predicted Temp: {temp:.2f}degree celsius")
    print("-----")