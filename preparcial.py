# ═══════════════════════════════════════════════════════════════
#  UNIVERSIDAD NACIONAL — SISTEMA DE BIBLIOTECA
#  Enfoque Bottom-Up con menú interactivo
# ═══════════════════════════════════════════════════════════════

class SistemaBiblioteca:
    def __init__(self, nombre_universidad):
        self.nombre_universidad = nombre_universidad
        self.libros    = {}   # { nombre_libro: estado }
        self.prestamos = {}   # { nombre_libro: {codigo, nombre} }
        self.contador  = 1    # código automático por orden de llegada

    # ── Agregar libro manualmente ──────────────────────────────
    def agregar_libro(self, nombre_libro):
        """
        Registra un libro nuevo en el sistema.
        Estado inicial siempre es 'biblioteca' (disponible).
        No permite duplicados.
        """
        if nombre_libro in self.libros:
            print(f"\n  ⚠️  '{nombre_libro}' ya está registrado.")
            return
        self.libros[nombre_libro] = "biblioteca"
        print(f"\n  📗 Libro agregado exitosamente: '{nombre_libro}'")

    # ── Día 1: prestar libro ───────────────────────────────────
    def prestar_libro(self, nombre_estudiante, nombre_libro):
        """
        Presta un libro asignando código automático al estudiante.
        Código se asigna en orden de llegada: 1, 2, 3, ...
        """
        # Verificar que el libro existe
        if nombre_libro not in self.libros:
            print(f"\n  ❌ El libro '{nombre_libro}' no existe en el sistema.")
            return

        # Verificar que esté disponible
        if self.libros[nombre_libro] == "prestamo":
            quien  = self.prestamos[nombre_libro]["nombre"]
            codigo = self.prestamos[nombre_libro]["codigo"]
            print(f"\n  ❌ '{nombre_libro}' ya está prestado.")
            print(f"     Lo tiene: {quien} (código {codigo})")
            return

        # Asignar código automático y registrar
        codigo_asignado       = self.contador
        self.contador        += 1
        self.libros[nombre_libro]    = "prestamo"
        self.prestamos[nombre_libro] = {
            "codigo": codigo_asignado,
            "nombre": nombre_estudiante
        }

        print(f"\n  ✅ PRÉSTAMO EXITOSO")
        print(f"  {'─'*38}")
        print(f"  Código asignado : {codigo_asignado}")
        print(f"  Estudiante      : {nombre_estudiante}")
        print(f"  Libro           : {nombre_libro}")
        print(f"  {'─'*38}")
        print(f"  ⚠️  Guarda tu código {codigo_asignado} para devolver el libro")

    # ── Día 4: devolver libro ──────────────────────────────────
    def devolver_libro(self, codigo_estudiante, nombre_libro):
        """
        Registra la devolución validando el código del estudiante.
        Solo puede devolver quien tiene el código correcto.
        """
        if nombre_libro not in self.libros:
            print(f"\n  ❌ El libro '{nombre_libro}' no existe en el sistema.")
            return

        if self.libros[nombre_libro] == "biblioteca":
            print(f"\n  ❌ '{nombre_libro}' no está prestado actualmente.")
            return

        codigo_registrado = self.prestamos[nombre_libro]["codigo"]
        nombre_registrado = self.prestamos[nombre_libro]["nombre"]

        if codigo_estudiante != codigo_registrado:
            print(f"\n  ❌ Código incorrecto.")
            print(f"     Este libro fue prestado con el código {codigo_registrado}.")
            return

        # Actualizar estado y limpiar registro
        self.libros[nombre_libro] = "biblioteca"
        del self.prestamos[nombre_libro]

        print(f"\n  ✅ DEVOLUCIÓN EXITOSA")
        print(f"  {'─'*38}")
        print(f"  Estudiante : {nombre_registrado} (código {codigo_estudiante})")
        print(f"  Libro      : {nombre_libro}")
        print(f"  Estado     : DISPONIBLE EN BIBLIOTECA")
        print(f"  {'─'*38}")

    # ── Semana 2: consultar inventario ─────────────────────────
    def consultar_inventario(self):
        """
        Muestra el estado completo de todos los libros:
        cuáles están disponibles y cuáles están prestados con quién.
        """
        if not self.libros:
            print("\n  ⚠️  No hay libros registrados en el sistema.")
            return

        disponibles = []
        en_prestamo = []

        for nombre_libro, estado in self.libros.items():
            if estado == "biblioteca":
                disponibles.append(nombre_libro)
            else:
                info = self.prestamos[nombre_libro]
                en_prestamo.append({
                    "libro":  nombre_libro,
                    "codigo": info["codigo"],
                    "nombre": info["nombre"]
                })

        print(f"\n  📚 INVENTARIO — {self.nombre_universidad}")
        print(f"  {'═'*50}")
        print(f"  Total libros : {len(self.libros)}")
        print(f"  Disponibles  : {len(disponibles)}")
        print(f"  En préstamo  : {len(en_prestamo)}")
        print(f"  {'═'*50}")

        print(f"\n  ✅ DISPONIBLES ({len(disponibles)})")
        print(f"  {'─'*50}")
        if disponibles:
            for libro in disponibles:
                print(f"  📗 {libro}")
        else:
            print("  (ninguno disponible)")

        print(f"\n  📤 EN PRÉSTAMO ({len(en_prestamo)})")
        print(f"  {'─'*50}")
        if en_prestamo:
            print(f"  {'Código':<10} {'Estudiante':<25} {'Libro'}")
            print(f"  {'─'*50}")
            for p in en_prestamo:
                print(f"  {p['codigo']:<10} {p['nombre']:<25} {p['libro']}")
        else:
            print("  (ningún libro en préstamo)")


# ═══════════════════════════════════════════════════════════════
#  MENÚ INTERACTIVO
# ═══════════════════════════════════════════════════════════════

def mostrar_menu():
    print(f"\n  {'═'*40}")
    print(f"   🏛️  BIBLIOTECA UNIVERSIDAD NACIONAL")
    print(f"  {'═'*40}")
    print(f"   1. Agregar libro")
    print(f"   2. Prestar libro")
    print(f"   3. Devolver libro")
    print(f"   4. Consultar inventario")
    print(f"   5. Salir")
    print(f"  {'═'*40}")
    print(f"   Selecciona una opción: ", end="")


def main():
    # Crear el sistema
    sistema = SistemaBiblioteca("Universidad Nacional")

    while True:
        mostrar_menu()
        opcion = input().strip()

        # ── Opción 1: Agregar libro ──────────────────────────
        if opcion == "1":
            print("\n  ── AGREGAR LIBRO ──")
            nombre_libro = input("  Nombre del libro: ").strip()
            if nombre_libro:
                sistema.agregar_libro(nombre_libro)
            else:
                print("  ⚠️  El nombre no puede estar vacío.")

        # ── Opción 2: Prestar libro ──────────────────────────
        elif opcion == "2":
            print("\n  ── PRÉSTAMO DE LIBRO ──")
            nombre_estudiante = input("  Nombre del estudiante: ").strip()
            nombre_libro      = input("  Nombre del libro     : ").strip()
            if nombre_estudiante and nombre_libro:
                sistema.prestar_libro(nombre_estudiante, nombre_libro)
            else:
                print("  ⚠️  Todos los campos son obligatorios.")

        # ── Opción 3: Devolver libro ─────────────────────────
        elif opcion == "3":
            print("\n  ── DEVOLUCIÓN DE LIBRO ──")
            try:
                codigo       = int(input("  Tu código de préstamo: ").strip())
                nombre_libro = input("  Nombre del libro     : ").strip()
                if nombre_libro:
                    sistema.devolver_libro(codigo, nombre_libro)
                else:
                    print("  ⚠️  El nombre del libro no puede estar vacío.")
            except ValueError:
                print("  ⚠️  El código debe ser un número entero.")

        # ── Opción 4: Consultar inventario ───────────────────
        elif opcion == "4":
            sistema.consultar_inventario()

        # ── Opción 5: Salir ──────────────────────────────────
        elif opcion == "5":
            print("\n  👋 Hasta luego — Sistema cerrado.\n")
            break

        # ── Opción inválida ──────────────────────────────────
        else:
            print("\n  ⚠️  Opción inválida. Elige entre 1 y 5.")


if __name__ == "__main__":
    main()