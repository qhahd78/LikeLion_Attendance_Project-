const date = new Date(); 

document.querySelector('#date-text').innerHTML = `
${date.getFullYear()}년 ${date.getMonth() +1}월 ${date.getDate()}일`;