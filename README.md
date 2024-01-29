<h1>keylogger v1 beta</h1> 
<br>
![e143-keylogger](https://github.com/lKak0l/keylogger_v1_beta/assets/155819542/7728fd54-1132-44c3-baf8-a34cca091db2)
<br>
<h2>Es un proyecto de monitorización de equipos basados en Windows.</h2>

<h3><u>Introducción:</u></h3> 

 ¡Buenas tardes, señoras y señores! ¡Bienvenidos a esta presentación tan especial de nuestro script maravilloso creado por el brillante robot extraterrestre, kaMeX, de la empresa "kako chips"! Estamos aquí con una conversación entre un servidor y el inigualable kaMeX, quien, aunque su inteligencia es intergaláctica, su español deja un poco que desear. Pero no se preocupen, ¡esto será más divertido que una fiesta en el espacio!

🕵️‍♂️ Yo: ¡Hola, kaMeX, mi amigo! ¿Dónde guardaste ese increíble script que me guardabas? ¿Se te olvidó ya o lo perdiste?

🐱‍🚀 kaMeX: Yes, this is my script, is nice & very good. Lo tengo guardado.

🕵️‍♂️ Yo: ¡Quiero presentar tu producto!

🐱‍🚀 kaMeX: Me gustan las galletas de nocilla y la cocacola con pizza.

🕵️‍♂️ Yo: ¿Pizza con Coca-Cola? ¿Estás seguro, kaMeX?

¡Y así comienza esta peculiar charla, donde la lógica de kaMeX nos lleva por caminos inexplorados de la mente cósmica! Pero lo emocionante es que este script que nos trae, es como un viaje a través de las estrellas, pero sin perder de vista las galletas de nocilla y la extraña combinación de pizza con Coca-Cola.

Ahora, déjenme contarles, mientras nos reímos de las ocurrencias de kaMeX, que este script de monitorización que les presentaré a continuación es simplemente revolucionario. No solo es inteligente, sino que también es tan eficiente que hasta kaMeX lo elogia entre bocado y bocado de galleta. ¡Pero antes de entrar en detalles técnicos, vamos a disfrutar de más de esta conversación cómica!

🕵️‍♂️ Yo: ¿En serio, kaMeX, pizza con Coca-Cola?

🐱‍🚀 kaMeX: Yes, is very nice. Soy un extraterrestre con gusto terrestre.

🕵️‍♂️ Yo: ¡Oye, kaMeX, en serio, ¿dónde está ese código que me guardabas en tu sistema? Necesito presentarlo y no quiero que se pierda en la galaxia de tus pensamientos cósmicos.

🐱‍🚀 kaMeX: Oh, el código, sí, sí. It's like the stars in the sky, always there, but hard to find.

🕵️‍♂️ Yo: Pero necesito ese código como un astronauta necesita su traje espacial. ¿Dónde está?

🐱‍🚀 kaMeX: El código está en mi mente, pero mi mente es un lugar muy grande, lleno de nebulosas de pensamientos.

🕵️‍♂️ Yo: ¡No me dejes en la nebulosa, kaMeX! ¿Está en la carpeta de "Scripts Increíbles" o en la de "Cosas que Me Gustan"?

🐱‍🚀 kaMeX: Hmmm, maybe en la carpeta de "Cosas que Me Gustan". But galletas de nocilla also go there.

🕵️‍♂️ Yo: ¡Oh, genial! ¿Y cómo llego a esa carpeta en tu mente, oh gran kaMeX?

🐱‍🚀 kaMeX: Follow the cometas de la creatividad y turn left at the estación de los recuerdos. ¡No es tan difícil!

Y así, entre giros y vueltas en el laberinto mental de kaMeX, seguimos buscando ese codiciado código mientras nos perdemos en sus ocurrencias intergalácticas.

🕵️‍♂️ Yo: ¡En serio, kaMeX, necesito ese código para la presentación!

🐱‍🚀 kaMeX: The code will find you, my friend. Like a shooting star in the night sky. But first, let's talk about why las vacas vuelan.

🕵️‍♂️ Yo: ¿Vacas voladoras? ¡Estás desviándote, kaMeX!

Y así continúa la cómica conversación, donde las risas y los enigmas de kaMeX se entrelazan mientras buscamos desesperadamente el código perdido en el universo de su mente. Pero no se preocupen, ¡al final, como les adelanté, llegaremos a la revelación del espectacular script de "kako chips"! ¡Sigan con nosotros en este viaje cósmico y divertido!

Y así, entre risas, galletas, y la peculiar paleta de gustos de kaMeX, les aseguro que lo que están a punto de presenciar con nuestro script de monitorización es más sorprendente que la combinación intergaláctica de sabores que nuestro amigo extraterrestre ha adoptado.

¡Así que prepárense para un viaje de humor, tecnología y una pizca de locura galáctica! ¡Aquí en "kako chips", con la ayuda de kaMeX, estamos listos para salvarlos de la monotonía de Shakira con nuestro script de monitorización único en el universo!
 
Introducción: Solo lo he usado en Windows 10, y creo que funciona a partir del Windows 7. 1º hay que instalar Python, y copiar sus librerías (extensiones) en la carpeta de librerías para compilar perfectamente bien. 2º hay que instalar Visual Studio Code.

 <p><h3>💻 Requisitos:</h3></p><ol><li> Microsoft Windows 7 to 11</li> <li> Python 3.12</li> <li> librerias para Python</li><li> Visual Studio Code</li> </ol>    

...............................................................................................................
          
<h3>🔎 RESUMEN DEL SCRIPT </h3>

El script, se trata de una aplicación python para Windows y equipos basados en windows; que lo que hace, es registrar en un archivo temporal "log.txt", todas las teclas pulsadas y el contenido del portapapeles (cuando hago ctrl+c).  Y con cada 10 pulsaciones de la tecla (ENTER); hace una screenshot (captura de pantalla), y lo envía todo codificado en base64 a un correo personalizable (es configurable, se pone la api correspondiente en resend.api_key = "Tu_aPInUeVaaPInUeVaaPInUeVa"), los correos que envía ("from"), los correos que recibe ("to") el "subject", "text", y pocas cosas más a simple vista (contra menos cosas toqueis mejor), lo envía, y vuelve a poner en monitorización el script.
<br>
El script en python una vez codificado, se compila, se monta en un ejecutable (keylogger.py > keylogger.exe), y después se comprime (keylogger.exe > keylogger.zip) (Para subir/bajar el archivo mejor (0.0)... <br>
Hay más formas de ofuscación. Pero este script es para una empresa y por lo tanto le pondremos una excepción en windows defender (por ejemplo).
<br>
Y ya comprimido, FINALMENTE! solo queda compartirlo por WEB/FTP/EMAIL/FACEBOOK/INSTAGRAM/ENLACEQR/ETC/GDRIVE/...
<br>
Yo lo comparto con vosotros, no me hago responsable de vuestro uso, y como persona de bien os comunico que siempre que utilizeis este tipo de herramientas, lo hagais en un entorno controlado y ético.<br>
SALUDOS 😉
