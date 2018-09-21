import math

pi = 3.141592653589793238462643383279502884197
rt2 = 1.41421356237309504880168872420969807856967
rt3 = 1.7320508075688772935274463415058723669428

class numApprox:
	def init(self):
		number = input();
		result = self.calc(number)

		if self.calc(number):
			print self.output(self.calc(number), "")

		elif self.calc(number/pi):
			print self.output(self.calc(number/pi), "*pi")

		elif self.calc(number*pi):
			print self.output(self.calc(number*pi), "/pi")

		elif self.calc(number/rt2):
			print self.output(self.calc(number/rt2), "*root 2")

		elif self.calc(number/rt3):
			print self.output(self.calc(number/rt3), "*root 3")

		else:
			print False


	def calc(self, x, error=0.00000001):
		n = int(math.floor(x))
		x -= n
		if x < error:
			return (n, 1)
		elif 1 - error < x:
			return (n+1, 1)

		nLow = 0
		dLow = 1

		nHigh = 1
		dHigh = 1

		nMid = nLow + nHigh
		dMid = dLow + dHigh
		solved = False

		while dMid <= 1000:
			nMid = nLow + nHigh
			dMid = dLow + dHigh

			if dMid * (x + error) < nMid:
				nHigh = nMid
				dHigh = dMid

			elif nMid < (x - error) * dMid:
				nLow = nMid
				dLow = dMid

			else:
				#solved = True
				return n * dMid + nMid, dMid

		if not solved:
			return False


	def output(self, result, multiplier):
		N, D = result
		return str(N) + " / " + str(D) + " " + multiplier


if __name__ == "__main__":
	numApprox().init()

