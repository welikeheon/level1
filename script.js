function submit () {
	var x = document.getElementById("n2").checked
	var data = {answers: x};
	
	fetch('/submit', {
		method: 'POST',
		headers: {'Content-Type': 'application/json'},
		body: JSON.stringify({ data })
	})
		.then(res => res.json())
		.then(ret => {
			document.getElementById("result") == "정답입니다"
		});
};
