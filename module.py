import re

def turn_txt_into_pig_latin(input_file, output_file):
    with open(input_file) as txt:
        lines = []
        for line in txt:
            translation = re.sub(r"([АЕЁИОУЫЭЮЯаеёиоуыэюя])", r"\1с\1", line)
            lines.append(translation)
        result = ''.join(lines)
    with open(output_file, "w") as out:
        out.write(result)