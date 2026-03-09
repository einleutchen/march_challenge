def dompier_music(switches):
  # Write code below 💖
  freq = [261, 294, 329, 349, 392, 440, 494, 523, 0]
  note = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5", "REST"]
  lib = list(zip(freq, note))
  decoded = list()

  for element in switches:
    binary = int(element[1:],2)
    for item in lib:
      if binary in item:
          decoded.append(item[-1])
  return decoded

print(dompier_music(["0100000101", "0100000101", "0110001000", "0110001000", "0110111000", "0110111000", "0110001000", "0000000000"]))
