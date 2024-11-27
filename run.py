import bojan

console = bojan.BojanConsole()
console.print("Message!", depth=0)
console.print("Nested message!", depth=1)
console.error("Nested error message!", depth=1)
console.save("log.bjn")