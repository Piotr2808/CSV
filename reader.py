import sys

class CsvReader:
    def __init__(self):
        self.input_file = sys.argv[1]
        self.output_file = sys.argv[2]
        self.task = []
        self.lines = self.read_file()
        for row in sys.argv[3:]:
            self.task.append(row.split(','))
    def read_file(self):
        lines = []
        with open(self.input_file, "r", encoding='utf-8') as file:
            for line in file.readlines():
                tmp = line.split('\n')[0].split(',')
                lines.append(tmp)

        return lines

    def change_file(self):
        for change in self.task:
            self.lines[int(change[0])][int(change[1])] = change[2]

    def save_file(self):
        with open(self.output_file, "w", encoding='utf-8') as file_to_save:
            for line in self.lines:
                for element in line[:-1]:
                    file_to_save.write(str(element) + ",")
                file_to_save.write(str(line[-1] + "\n"))

read = CsvReader()
read.read_file()
print(read.lines)
read.change_file()
print(read.lines)
read.save_file()