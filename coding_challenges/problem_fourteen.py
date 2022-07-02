# *Problem 14*. Count the word frequencies in this sentence and store it in a dictionary.
# ``sonnet1 = [’from’, ’fairest’, ’creatures’, ’we’, ’desire’, ’
# increase’,’that’, ’thereby’, ’beauty’,’rose’, ’might’,’
# never’, ’die’,’but’,’as’, ’the’, ’riper’, ’should’, ’by’,
# ’time’, ’decease’,’his’, ’tender’, ’heir’, ’might’, ’
# bear’, ’his’, ’memory’,’but’,’thou’, ’contracted’, ’to’,
# ’thine’, ’own’, ’bright’,’eyes’,’feed’,’thy’,’light’, ’
# flame’, ’with’,’self-substantial’,’fuel’,’making’,’a’,’
# famine’,’where’, ’abundance’,’lies’,’thyself’,’thy’,’foe’
# , ’to’, ’thy’, ’sweet’, ’self’, ’too’, ’cruel’]``
 

def CountFrequency(sonnet1):

	# Creating an empty dictionary
	freq = {}
	for item in sonnet1:
		if (item in freq):
			freq[item] += 1
		else:
			freq[item] = 1

	for key, value in freq.items():
		print(f'{key}: {value}')

# Driver function
if __name__ == "__main__":

	sonnet1 = ['from', 'fairest', 'creatures', 'we', 'desire', 'increase','that', 
            'thereby', 'beauty','rose', 'might','never', 'die','but','as', 
            'the', 'riper', 'should', 'by','time', 'decease','his', 'tender', 
            'heir', 'might', 'bear', 'his', 'memory','but','thou', 'contracted', 
            'to','thine', 'own', 'bright','eyes','feed','thy','light', 'flame', 
            'with','self-substantial','fuel','making','a','famine','where', 
            'abundance','lies','thyself','thy','foe', 'to', 'thy', 'sweet', 
            'self', 'too', 'cruel']

    # Calling function
	CountFrequency(sonnet1)

