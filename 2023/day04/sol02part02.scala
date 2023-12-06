import scala.math.pow
import scala.io.Source

object sol02part02:
	def main(args: Array[String]) =
		val source = Source.fromFile("./2023/day04/input.txt")
		val lines = source
			.getLines
			.toList
		
		val sol = "tbd"

			
		
		println(sol)

	def getScore(s: String): Int =
		val pattern = """Card.*(\d+): ([\d\s]+) \| ([\d\s]+)""".r
		s match
			case pattern(cardId, winners, numbers) =>
				val winnersSet = winners.trim.split("\\s+").toSet
				val numbersSet = numbers.trim.split("\\s+").toSet
				winnersSet.intersect(numbersSet).size.toInt
			case _ =>
				throw new Exception("Invalid input")
