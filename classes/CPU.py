from helpers.charts import draw_horizontal_bar_chart


class CPU():
    def __init__(self, id):
        self.proc = []
        self.free_at = 0
        self.id = id


    def assign(self, process):
        self.proc.append(process)
        self.free_at += process

    def remove(self, process):
        self.proc.remove(process)
        self.free_at -= process

    def getProcesses(self):
        return self.proc

    def getFreeAt(self):
        return self.free_at

    def getUsage(self, max_time):
        return (self.free_at / max_time) * 100

    def clear(self):
        self.proc = []
        self.free_at = 0


def drawChart(CPUs):
    times = [cpu.getFreeAt() for cpu in CPUs]
    cpu_No = [str(id + 1) for id, value in enumerate(CPUs)]
    draw_horizontal_bar_chart(cpu_No, times)
