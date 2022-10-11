training_dataset = [
    "¿Cuál es su misión?",
    "Nuestra misión es impulsar el florecimiento humano promoviendo la libertad individual y los principios judeocristianos.",
    
    "¿Creen en Dios",
    "Creemos en que Dios es el creador providente de todas las cosas. Dios es la primera y máxima realidad. Es un Dios verdadero, vivo, creador del cielo y de la tierra, omnipresente y omnisciente. Nos creó y estableció una alianza con nosotros. Le llamamos Padre porque lo reconocemos como una autoridad trascendente que nos ama.",

    "¿En qué fundamentan la dignidad de la persona humana?",
    "La dignidad de la persona deriva de su condición de hijo de Dios. Dios creó al ser humano a Su imagen: libre y responsable. Nuestra dignidad inherente deriva de nuestra filiación divina y no de nuestras características físicas, estatus social, posesiones materiales u otros atributos. Estamos llamados por Dios a ser compasivos y caritativos unos con otros, partiendo, no de la imposición, sino de acciones libres y responsables.",
    
    "¿Creen que existe la verdad?",
    "Existe la verdad y el hombre es capaz de conocerla. Las personas, dotadas de inteligencia, somos capaces de aprehender la verdad sobre el mundo que nos rodea, aunque siempre de forma imperfecta. A través del estudio y del diálogo con otras personas, discernimos la verdad. La verdad revelada por Dios nos permite aproximarnos al conocimiento de Dios y su creación.”,
    
    "¿Qué caracteriza a la persona humana?",
    "La persona es libre, responsable y social por naturaleza. Las personas expresamos, a través de nuestros actos, nuestras preferencias y capacidades cuando elegimos en libertad los bienes morales que nos potencian. Las personas libres y responsables asumimos las consecuencias positivas y negativas de nuestras elecciones. Somos cocreadores de cultura, instituciones y riqueza, sobre todo cuando cooperamos pacíficamente con otros. La cooperación entre las personas depende de la igualdad ante la ley, de la prueba y error como factor correctivo y así mismo, de la libertad (del mecanismo) de precios que sintetizan información (informa) sobre la escasez relativa de los bienes y su demanda.”,
    
    "¿Qué es el pecado?",
    "El pecado es una realidad. El pecado es una realidad histórica que nos afecta en el tiempo y en el espacio. Los hombres no tenemos conocimiento perfecto de lo que ocurre a nuestro alrededor y solo podemos atenernos al aprendizaje frente al conocimiento disperso de factores, necesidades y procesos. Es de mejor calidad la información que sustenta nuestras elecciones en un entorno libre que en un entorno coercitivo y centralizado, aunque nunca será perfecta. A veces, las personas elegimos el mal; pero si somos libres, podemos reconocer nuestra falta, pedir perdón y rectificar",
    
    "¿De qué depende el florecimiento material?",
    "El florecimiento material depende de la creación de riqueza. Las personas prosperan cuando producen, consumen e intercambian libremente con los demás. Los intercambios voluntarios permiten a las personas expresar su naturaleza creativa. Convierten las transacciones que pudieran ser juegos de suma cero, donde la ganancia de uno es a costillas del otro, en transacciones mutuamente ventajosas.  El florecimiento humano requiere que la comunidad y sus gobernantes respeten los derechos de propiedad privada, la libertad de contratos y el Estado de Derecho. Dichas instituciones potencian la creación de riqueza.",
    
    "¿Somos todos iguales?",
    "“Todos los seres humanos son iguales ante la ley. Recibimos de Dios los dones de la vida, la libertad y la propiedad. La igualdad ante la ley de los gobernados se inspira en la igualdad de todas las criaturas humanas a ojos de Dios Padre. Muchos textos constitucionales coinciden con la tradición judeocristiana en reconocer la propiedad, la vida y la libertad de los hombres, como derechos anteriores y superiores al estado.  El principio de subsidiariedad fortalece al estado de derecho por cuanto busca evitar que el aparato gubernamental usurpe aquellas funciones que deben ser desempeñadas por la persona individual y las instituciones que le son más inmediatas, y porque reduce la asistencia estatal únicamente a aquellas instancias en que las personas individuales y las instituciones que le son más inmediatas no han sido capaces de desempeñar las funciones que les son propias.",
    
    "¿Qué piensan de la familia?",
    "La familia es el fundamento de la sociedad. Una familia es una sociedad natural y el fundamento de la sociedad, cuyo derecho a existir es sustentado por la ley divina. La familia es una comunidad de personas conformada por padre, madre e hijos.  Las sagradas escrituras resaltan la relevancia de la familia: nos instan a honrar a padre y a madre y describen como modelo a la Sagrada Familia, conformada por José, María y Jesús. Las personas que tienen vocación al matrimonio y a la paternidad reciben la gracia y acompañamiento de Dios para honrar el compromiso matrimonial a ser fiel y a honrar y respetar a la pareja elegida, y para formar y educar a sus hijos en el amor y la fe.",
    
    "¿De qué depende el futuro de nuestra civilización?",
    "El futuro de la civilización depende de la cultura de la libertad. Si la persona humana tiene un origen y un destino trascendente, entonces un entorno cultural que reconoce esta verdad conduce al florecimiento humano. La cultura de la libertad y de la vida produce orden y armonía entre los miembros de la comunidad, y la familia es la principal transmisora de dicha cultura. Con frecuencia, las personas creyentes entran en tensión con la cultura popular, o la cultura secular, la cual puede alejarnos de Dios, de lo bello y del bien, y suele tomar matices intolerantes. Creemos que es necesario rescatar los valores judeo-cristianos que constituyen los cimientos de la civilización occidental, incluyendo el valor del pluralismo y el respeto a quienes tienen convicciones diferentes a las nuestras.",
    
    "¿Qué valoran?",
    "Valoramos la Veracidad. Es la virtud que nos lleva a buscar, en todo y ante todo, la verdad y a defenderla con valor. La persona veraz es sincera, honesta, franca y tiene buena fe. Sabe escuchar y respetar las opiniones del prójimo. La Libertad. La persona libre posee la facultad natural para pensar y actuar según su voluntad ordenada al bien. Ser libre implica ser responsable. La Integridad. La persona íntegra es de una sola pieza: recta, confiable, coherente y honesta. Piensa lo que vive y vive lo que piensa. La Humildad. La persona humilde se reconoce como un ser creado, herido por el pecado pero amado infinitamente por Dios. La Tolerancia. La persona tolerante sabe que existen diferentes criterios y tiene capacidad de debatir con el otro con paciencia y comprensión. Distingue entre el respeto a la persona y sus ideas, creencias o prácticas, que pueden o no ser erróneas."

]
{
    'import_path': 'chatterbot.logic.SpecificResponseAdapter',
    'input_text': 'Help',
    'output_text': 'Ok, here is a link: https://vakilsearch.com/'
}
