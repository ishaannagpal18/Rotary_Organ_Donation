const canvas = document.getElementById('canvas')
const ctx = canvas.getContext('2d')
const nameInput = document.getElementById('name')
const downloadBtn = document.getElementById('download-btn')
  let name = document.getElementById("p").innerHTML;
  let auth_token = document.getElementById("p1").innerHTML;
  let age = document.getElementById("p2").innerHTML;
  let gender = document.getElementById("p3").innerHTML;
  let blood_group = document.getElementById("p4").innerHTML;
  let tel = document.getElementById("p5").innerHTML;
  let email = document.getElementById("p6").innerHTML;
  let heart = document.getElementById("p7").innerHTML;
  let kidneys = document.getElementById("p8").innerHTML;
  let corneas_or_eye_balls = document.getElementById("p9").innerHTML;
  let lungs = document.getElementById("p10").innerHTML;
  let skin = document.getElementById("p11").innerHTML;
  let pancreas = document.getElementById("p12").innerHTML;
  let liver = document.getElementById("p13").innerHTML;
  let all_organs = document.getElementById("p14").innerHTML;
  let date = document.getElementById("p15").innerHTML;
  let myFont = new FontFace(
    "Bebas Neue",
    "url(https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap)"
  );


const image = new Image()
image.src = '/static/img/Donor_card-01.png'
image.onload = function () {
	drawImage()
}



function drawImage() {
	// ctx.clearRect(0, 0, canvas.width, canvas.height)
	ctx.drawImage(image, 0, 0, canvas.width, canvas.height)
	ctx.font = 'bold 25px Bebas Neue'
	ctx.fillStyle = '#1B1A17'
  ctx.fillText(date, 106, 556)
	ctx.fillText(name, 130, 616)
  ctx.fillText(auth_token, 200, 183)
  ctx.fillText(age, 130, 665)
  ctx.fillText(gender, 290, 665)
  ctx.fillText(blood_group, 530, 665)
  ctx.fillText(tel, 220, 708)
  ctx.fillText(email, 250, 755)
  const organ = (heart!="None") ?[ctx.fillRect(354, 864, 12, 12)]:
  (kidneys!="None") ?[ctx.fillRect(136, 823, 12, 12)]:
  (corneas_or_eye_balls!="None") ?[ctx.fillRect(247.5, 823, 12, 12)]:
  (lungs!="None") ?[ctx.fillRect(338, 823, 12, 12)]:
  (skin!="None") ?[ctx.fillRect(419, 823, 12, 12)]:
  (pancreas!="None") ?[ctx.fillRect(153, 864, 12, 12)]:
  (liver!="None") ?[ctx.fillRect(264, 864, 12, 12)]:
  (all_organs!="None") ?[ctx.fillRect(435.5, 864, 12, 12)]:
  alert("no")
  const organ1 =
  (kidneys!="None") ?[ctx.fillRect(136, 823, 12, 12)]:
  (corneas_or_eye_balls!="None") ?[ctx.fillRect(247.5, 823, 12, 12)]:
  (lungs!="None") ?[ctx.fillRect(338, 823, 12, 12)]:
  (skin!="None") ?[ctx.fillRect(419, 823, 12, 12)]:
  (pancreas!="None") ?[ctx.fillRect(153, 864, 12, 12)]:
  (liver!="None") ?[ctx.fillRect(264, 864, 12, 12)]:
  (all_organs!="None") ?[ctx.fillRect(435.5, 864, 12, 12)]:
  null
  const organ2 =
  (corneas_or_eye_balls!="None") ?[ctx.fillRect(247.5, 823, 12, 12)]:
  (lungs!="None") ?[ctx.fillRect(338, 823, 12, 12)]:
  (skin!="None") ?[ctx.fillRect(419, 823, 12, 12)]:
  (pancreas!="None") ?[ctx.fillRect(153, 864, 12, 12)]:
  (liver!="None") ?[ctx.fillRect(264, 864, 12, 12)]:
  (all_organs!="None") ?[ctx.fillRect(435.5, 864, 12, 12)]:
  null
  const organ3 =
  (lungs!="None") ?[ctx.fillRect(338, 823, 12, 12)]:
  (skin!="None") ?[ctx.fillRect(419, 823, 12, 12)]:
  (pancreas!="None") ?[ctx.fillRect(153, 864, 12, 12)]:
  (liver!="None") ?[ctx.fillRect(264, 864, 12, 12)]:
  (all_organs!="None") ?[ctx.fillRect(435.5, 864, 12, 12)]:
  null
  const organ4 =
  (skin!="None") ?[ctx.fillRect(419, 823, 12, 12)]:
  (pancreas!="None") ?[ctx.fillRect(153, 864, 12, 12)]:
  (liver!="None") ?[ctx.fillRect(264, 864, 12, 12)]:
  (all_organs!="None") ?[ctx.fillRect(435.5, 864, 12, 12)]:
  null
  const organ5 =
  (pancreas!="None") ?[ctx.fillRect(153, 864, 12, 12)]:
  (liver!="None") ?[ctx.fillRect(264, 864, 12, 12)]:
  (all_organs!="None") ?[ctx.fillRect(435.5, 864, 12, 12)]:
  null
  const organ6 =
  (liver!="None") ?[ctx.fillRect(264, 864, 12, 12)]:
  (all_organs!="None") ?[ctx.fillRect(435.5, 864, 12, 12)]:
  null
  const organ7 =
  (all_organs!="None") ?[ctx.fillRect(435.5, 864, 12, 12)]:
  null

}


// nameInput.addEventListener('input', function () {
// 	drawImage()
// })

downloadBtn.addEventListener('click', function () {
	downloadBtn.href = canvas.toDataURL('image/jpg')
	downloadBtn.download = 'Donor Card-' + name
})
