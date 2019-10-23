from helpers.charts import draw_horizontal_bar_chart


class CPU():
    def __init__(self):
        self.proc = []
        self.free_at = 0

    def assign(self, process):
        self.proc.append(process)
        self.free_at += process

    def getProcesses(self):
        return self.proc

    def getFreeAt(self):
        return self.free_at

    def getUsage(self, max_time):
        return (self.free_at / max_time) * 100


def drawChart(CPUs):
    times = [cpu.getFreeAt() for cpu in CPUs]
    cpu_No = [str(id) for id, value in enumerate(CPUs)]
    draw_horizontal_bar_chart(cpu_No, times)
