class Stationery:
    title = None

    def draw(self):
        print("Запуск отрисовки")


class Pencil(Stationery):
    title = "Карандаш"

    def draw(self):
        super().draw()
        print("Отрисовка карандашом")


class Pen(Stationery):
    title = "Ручка"

    def draw(self):
        super().draw()
        print("Отрисовка ручкой")


class Handle(Stationery):
    title = "Маркер"

    def draw(self):
        super().draw()
        print("Отрисовка маркером")


pencil = Pencil()
pen = Pen()
handle = Handle()
pencil.draw()
pen.draw()
handle.draw()
