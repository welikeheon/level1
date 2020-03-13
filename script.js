function submit () {
	let answer = document.querySelectorAll('input[name="answer"]:checked')
	let values = [];

	Array.prototype.forEach.call(answer, (elem) => {
		values.push(elem.value);
	})


	let data = {answers: values};
	
	fetch('/submit', {
		method: 'POST',
		headers: {'Content-Type': 'application/json'},
		body: JSON.stringify(data)
	})
	.then(res => res.text)
	.then(res => {
		if (res == "true") {
			document.getElementById('result').innerHTML='정답입니다.';
		} else {
			document.getElementById('result').innerHTML='오답입니다.';
		}
	});
};
