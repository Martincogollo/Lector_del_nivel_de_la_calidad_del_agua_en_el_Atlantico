entrada = input().split(" ")
entrada = list(map(int,entrada))
entrada = sorted(entrada)

for i in entrada:
    ciudad = ""
    departamento = ""
    mujeres = 0
    hombres = 0
    pacientes = 0
    medicamentos = 0
    archivo = open("data.csv")  
    next(archivo)
    for linea in archivo:
        datos = linea.split(",")

        if int (datos[5]) >= 1 and int(datos[32]) and int(datos[5]) == i:
          if len(departamento == 0 or len(ciudad)) ==0:
            departamento = datos[4]
            ciudad = datos[3]
          if int (datos[8]< 91 and int (datos[8])) < 63:
                if datos[2].lower() == "m":
                    hombres = hombres +1
                if datos[2].lower() == "f":
                    mujeres = mujeres +1
                pacientes = pacientes +1
                medicamentos = medicamentos + int(datos[7])
          elif (int(datos[8]) >= 91 and int(datos[8]) < 134) and (int(datos[9]) >= 63 and int(datos[9]) < 77):
                 continue

          elif (int(datos[8]) >= 134 and int(datos[8]) < 162) and (int(datos[9]) >= 77 and int(datos[9]) < 105):
                 continue
          elif (int(datos[8]) >= 162 and int(datos[8]) < 188) and (int(datos[9]) >= 105 and int(datos[9]) < 119):
                if datos[2].lower() == "m":
                    hombres = hombres +1
                if datos[2].lower() == "f":
                    mujeres = mujeres +1
                pacientes = pacientes +1
                medicamentos = medicamentos + int(datos[7])
          elif (int(datos[8]) >= 188 and int(datos[8]) < 201) and (int(datos[9]) >= 119 and int(datos[9]) < 126):
                if datos[2].lower() == "m":
                    hombres = hombres +1
                if datos[2].lower() == "f":
                    mujeres = mujeres +1
                pacientes = pacientes +1
                medicamentos = medicamentos + int(datos[7])
          elif (int(datos[8]) >= 201 and int(datos[8]) < 214) and (int(datos[9]) >= 126 and int(datos[9]) < 146):
                if datos[2].lower() == "m":
                    hombres = hombres +1
                if datos[2].lower() == "f":
                    mujeres = mujeres +1
                pacientes = pacientes +1
                medicamentos = medicamentos + int(datos[7])
          elif int(datos[9]) < 77:
                if datos[2].lower() == "m":
                    hombres = hombres +1
                if datos[2].lower() == "f":
                    mujeres = mujeres +1
                pacientes = pacientes +1
                medicamentos = medicamentos + int(datos[7])
          else:
                if datos[2].lower() == "m":
                    hombres = hombres +1
                if datos[2].lower() == "f":
                    mujeres = mujeres +1
                pacientes = pacientes +1
                medicamentos = medicamentos + int(datos[7])
                
    print("{0} {1} {2}".format(i, ciudad, departamento))
    print("schuled patients")
    print("male {0} ".format(hombres))
    print("female {0} ".format(mujeres))
    print("total {0} ".format(pacientes))
    print("schuduled medicine quantity")
    mean = float(medicamentos)/pacientes
    print("mean {0:.2f}".format(mean))
    print("total {0}".format(medicamentos))
    archivo.close()