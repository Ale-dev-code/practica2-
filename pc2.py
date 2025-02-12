class Conductor:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.horarios = []  

    def agregar_horario(self, hora: str):
        if hora not in self.horarios:
            self.horarios.append(hora)
            return True
        return False


class Bus:
    def __init__(self, placa: str):
        self.placa = placa
        self.ruta = None
        self.horarios = []  
        self.conductor_asignado = None

    def asignar_ruta(self, ruta: str):
        self.ruta = ruta

    def agregar_horario(self, hora: str):
        if hora not in self.horarios:
            self.horarios.append(hora)
            return True
        return False

    def asignar_conductor(self, conductor):
        self.conductor_asignado = conductor


class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self, placa: str):
        if not placa:
            print("La placa no puede estar vacía.")
            return

        if any(bus.placa == placa for bus in self.buses):
            print(f"Ya existe un bus con la placa {placa}.")
            return

        bus = Bus(placa)
        self.buses.append(bus)
        print(f"Bus con placa {placa} agregado exitosamente.")

    def agregar_conductor(self, nombre: str):
        if not nombre:
            print("El nombre del conductor no puede estar vacío.")
            return

        if any(conductor.nombre == nombre for conductor in self.conductores):
            print(f"Ya existe un conductor con el nombre {nombre}.")
            return

        conductor = Conductor(nombre)
        self.conductores.append(conductor)
        print(f"Conductor {nombre} agregado exitosamente.")

    def agregar_ruta_a_bus(self, placa: str, ruta: str):
        bus = next((bus for bus in self.buses if bus.placa == placa), None)

        if not bus:
            print(f"No se encontró un bus con la placa {placa}.")
            return

        bus.asignar_ruta(ruta)
        print(f"Ruta '{ruta}' asignada al bus {placa}.")

    def agregar_horario_a_bus(self, placa: str, hora: int):
        if hora < 0 or hora > 23:
            print("El horario debe estar entre 0 y 23 horas.")
            return

        bus = next((bus for bus in self.buses if bus.placa == placa), None)

        if not bus:
            print(f"No se encontró un bus con la placa {placa}.")
            return

        if bus.agregar_horario(f"{hora}:00"):
            print(f"Horario {hora}:00 agregado al bus {placa}.")
        else:
            print(f"El horario {hora}:00 ya está asignado al bus {placa}.")

    def agregar_horario_a_conductor(self, nombre: str, hora: int):
        if hora < 0 or hora > 23:
            print("El horario debe estar entre 0 y 23 horas.")
            return

        conductor = next((conductor for conductor in self.conductores if conductor.nombre == nombre), None)

        if not conductor:
            print(f"No se encontró un conductor con el nombre {nombre}.")
            return

        if conductor.agregar_horario(f"{hora}:00"):
            print(f"Horario {hora}:00 agregado al conductor {nombre}.")
        else:
            print(f"El horario {hora}:00 ya está asignado al conductor {nombre}.")

    def asignar_bus_a_conductor(self, placa: str, nombre: str, hora: int):
        if hora < 0 or hora > 23:
            print("El horario debe estar entre 0 y 23 horas.")
            return

        bus = next((b for b in self.buses if b.placa == placa), None)
        conductor = next((c for c in self.conductores if c.nombre == nombre), None)

        if not bus:
            print(f"No se encontró un bus con la placa {placa}.")
            return

        if not conductor:
            print(f"No se encontró un conductor con el nombre {nombre}.")
            return

        if f"{hora}:00" in conductor.horarios:
            print(f"El conductor {nombre} ya tiene asignado el horario {hora}:00.")
            return

        if f"{hora}:00" in bus.horarios:
            print(f"El bus {placa} ya tiene asignado el horario {hora}:00.")
            return

        conductor.agregar_horario(f"{hora}:00")
        bus.agregar_horario(f"{hora}:00")
        bus.asignar_conductor(conductor)
        print(f"Bus {placa} asignado al conductor {nombre} en el horario {hora}:00.")


def menu():
    admin = Admin()

    while True:
        print("\n--- Menú ---")
        print("1. Agregar bus")
        print("2. Agregar conductor")
        print("3. Asignar ruta a bus")
        print("4. Registrar horario a bus")
        print("5. Registrar horario a conductor")
        print("6. Asignar bus a conductor")
        print("7. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            placa = input("Ingrese la placa del bus: ").strip()
            if placa:
                admin.agregar_bus(placa)
            else:
                print("La placa no puede estar vacía.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del conductor: ").strip()
            if nombre:
                admin.agregar_conductor(nombre)
            else:
                print("El nombre no puede estar vacío.")

        elif opcion == "3":
            placa = input("Ingrese la placa del bus: ").strip()
            ruta = input("Ingrese la ruta del bus: ").strip()
            if placa and ruta:
                admin.agregar_ruta_a_bus(placa, ruta)
            else:
                print("La placa y la ruta no pueden estar vacías.")

        elif opcion == "4":
            placa = input("Ingrese la placa del bus: ").strip()
            try:
                hora = int(input("Ingrese el horario (0-23): ").strip())
                if placa:
                    admin.agregar_horario_a_bus(placa, hora)
                else:
                    print("La placa no puede estar vacía.")
            except ValueError:
                print("Debe ingresar un número válido para el horario.")

        elif opcion == "5":
            nombre = input("Ingrese el nombre del conductor: ").strip()
            try:
                hora = int(input("Ingrese el horario (0-23): ").strip())
                if nombre:
                    admin.agregar_horario_a_conductor(nombre, hora)
                else:
                    print("El nombre no puede estar vacío.")
            except ValueError:
                print("Debe ingresar un número válido para el horario.")

        elif opcion == "6":
            placa = input("Ingrese la placa del bus: ").strip()
            nombre = input("Ingrese el nombre del conductor: ").strip()
            try:
                hora = int(input("Ingrese el horario (0-23): ").strip())
                if placa and nombre:
                    admin.asignar_bus_a_conductor(placa, nombre, hora)
                else:
                    print("La placa y el nombre no pueden estar vacíos.")
            except ValueError:
                print("Debe ingresar un número válido para el horario.")

        elif opcion == "7":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()

