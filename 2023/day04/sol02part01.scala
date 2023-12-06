import scala.math.pow
import scala.io.Source

object sol02part01:
	def main(args: Array[String]) =
		val source = Source.fromFile("./2023/day04/input.txt")
		val sol = source
			.getLines
			.map(getScore)
			.filter(_ > 1)
			.sum
			.toInt
		
		println(sol)

	def getScore(s: String): Double =
		val pattern = """Card.*(\d+): ([\d\s]+) \| ([\d\s]+)""".r
		s match
			case pattern(cardId, winners, numbers) =>
				val winnersSet = winners.trim.split("\\s+").toSet
				val numbersSet = numbers.trim.split("\\s+").toSet
				val count = winnersSet.intersect(numbersSet).size
				pow(2, count-1)
			case _ =>
				throw new Exception("Invalid input")
