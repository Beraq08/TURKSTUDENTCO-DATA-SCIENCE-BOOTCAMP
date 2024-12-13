class Task:
    def __init__(self, name):
        self.name = name
        self.tamamlandi = False

    def __str__(self):
        return self.name


class TaskManager:
    def __init__(self):
        self.tamamlanmayanlar = []
        self.tamamlananlar = []

    def gorev_ekle(self, task):
        if task not in self.tamamlanmayanlar and task not in self.tamamlananlar:
            self.tamamlanmayanlar.append(task)
            return f"{task} görevi eklendi"
        else:
            return f"{task} daha önce eklendi"

    def gorev_tamamla(self, task):
        if task in self.tamamlanmayanlar:
            task.tamamlandi = True
            self.tamamlanmayanlar.remove(task)
            self.tamamlananlar.append(task)
            return f"{task} görevi tamamlandı"
        else:
            return f"Görev yok veya zaten tamamlanmış"

    def gorev_sil(self, task):
        if task in self.tamamlanmayanlar:
            self.tamamlanmayanlar.remove(task)
            return f"{task} görevi silindi"
        elif task in self.tamamlananlar:
            self.tamamlananlar.remove(task)
            return f"{task} görevi silindi"
        else:
            return f"{task} görevi bulunamadı"

    def gorev_listesi(self):
        if self.tamamlanmayanlar or self.tamamlananlar:
            f=open("gorevler.txt", "w") 
            f.write(f"Tamamlanan görevler: {[str(task) for task in self.tamamlananlar]}\n")
            f.write(f"Tamamlanmayan görevler: {[str(task) for task in self.tamamlanmayanlar]}\n")
            return f"Tamamlanan görevler: {[str(task) for task in self.tamamlananlar]} Tamamlanmayan görevler: {[str(task) for task in self.tamamlanmayanlar]}"
        else:
            return "Hiç görev eklenmedi"

#Task sınıfı görev özelliklerini tutuyor, TaskManager ile görev ekleme,silme,tamamlama ve liste çıkarma işlemlerini yapıyoruz

gorevler = TaskManager()


gorev1 = Task("Ödev")
gorev2 = Task("Sınav")

print(gorevler.gorev_ekle(gorev1))
print(gorevler.gorev_ekle(gorev2))
print(gorevler.gorev_listesi())
print(gorevler.gorev_tamamla(gorev1))
print(gorevler.gorev_listesi())
