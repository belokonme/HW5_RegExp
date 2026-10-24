import re

def turn_txt_into_pig_latin(input_file):
    with open(input_file) as txt:
        lines = []
        for line in txt:
            translation = re.sub(r"([АЕЁИОУЫЭЮЯаеёиоуыэюя])", r"\1с\1", line)
            lines.append(translation)
        result = ''.join(lines)
    return lines


def get_song_chords(input_file):
    with open(input_file) as song:
        chords = set()
        for line in song:
            result = re.findall(r"\b([CDEFGAHB][#b]?m?[1-9]?(?:/[CDEFGAHB][#b]?)?)(?:\s|$)", line)
            chords.update(result)
    return chords

