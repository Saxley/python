time_course={
    "max" : 7,
    "min" : 2.5,
    "mean" : 4,
    "dalton" : 1.5
}
def dif_percent(list):
    list_timer = []
    list_percent = []
    hour_minutes = 60
    for value in list.items():
        minutes = value[1] * hour_minutes
        list_timer.append(minutes)
    list_timer.sort()
    for item in list_timer:
        list_percent.append(item * 100 / list_timer[-1])
    return list_percent

def text(name_course, percent, time):
    print(f"Porcentaje del curso de {name_course} : {percent:.2f}% con duración de {time} horas.")

def dashboard_result(time_course):
    list_percent = dif_percent(time_course)
    titulo = "Diferencia porcentual en tiempo de explicación entre cursos."
    min = list_percent[0]
    major = list_percent[-1]
    min_internet = 0
    for time in list_percent:
        if time == min:
            text("Dalton", time, time_course.get("dalton"))
        if time == major:
            text("Mayor", time, time_course.get("max"))
        if time < major and time > min:
            text("Menor", time, time_course.get("min"))
            min_internet = time
        if time < major and time > min_internet and min_internet > 0:
            text("Promedio", time, time_course.get("mean"))
        print(f"La diferencia porcentual con el más tardado es de {major - time:.2f}%.")
        print(f"La diferencia porcentual con el más rapido es de {time - min:.2f}%.\n")

if __name__ == "__main__":
    dashboard_result(time_course)


        
#print(dir(time_course))