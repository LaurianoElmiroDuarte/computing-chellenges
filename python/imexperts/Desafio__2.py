parentheseOpen = '('
parentheseClose = ')'
bracketOpen = '['
bracketClose = ']'
braceOpen = '{'
braceClose = '}'

	checkIsBalanced = (oneString)
	littleStack = []

	if (oneString.length % 2) is not 0:
		return 'NAO'


	for i = 0 i < oneString.length i++
			def  parentheseOpen():
				littleStack.append(parentheseOpen)
				break
			def bracketOpen():
				littleStack.append(bracketOpen)
				break
			def braceOpen():
				littleStack.append(braceOpen)
				break
			def parentheseClose():
				if littleStack == []) {
					return 'NAO'
				}
				if littleStack.pop() not = parentheseOpen) {
					return 'NAO'
				}
				break
			def bracketClose:
				if littleStack == []) {
					return 'NAO'
				}
				if littleStack.pop() not = bracketOpen) {
					return 'NAO'
				}
				break
			def braceClose:
				if littleStack == []) {
					return 'NAO'
				}
				if littleStack.pop() not = braceOpen:
					return 'NAO'

				break

	
			return 'SIM'


print(checkIsBalanced('{[()]}'))
print(checkIsBalanced('{[(])}'))
print(checkIsBalanced('{{[[(())]]}}'))
