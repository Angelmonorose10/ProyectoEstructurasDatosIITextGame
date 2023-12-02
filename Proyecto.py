import time
import random


def mostrar_ascii_art():
    print("######    #####    #####   ######    #####   ##   ##")
    print("##  ##  ##   ##  ##   ##  # ## #   ##   ##  ###  ##")
    print("##  ##  ##   ##  #          ##     ##   ##  #### ##")
    print("#####   ##   ##   #####     ##     ##   ##  ## ####")
    print("##  ##  ##   ##       ##    ##     ##   ##  ##  ###")
    print("##  ##  ##   ##  ##   ##    ##     ##   ##  ##   ##")
    print("######    #####    #####    ####     #####   ##   ## ")


def mostrar_intro():
    print(
        "Me desperté de repente, como si el universo entero hubiera conspirado para interrumpir mi sueño. Eran las tres de la madrugada, y un silencio inusual pesaba en el aire. Pero no era el silencio que trae la calma; era la ominosa quietud que preludia el desastre. Me incorporé en la cama, escuchando con atención los ruidos tenues que llegaban desde la oscuridad."
    )
    print("")

    print(
        "El hogar, una fortaleza que antes consideraba segura, se transformó en un laberinto de sombras siniestras. Mis padres dormían, ajenos a los sonidos que me habían arrancado de mis sueños. Al levantarme, noté la ausencia de la luz de la luna que normalmente filtraba a través de las cortinas, arrojando un velo plateado sobre los rincones familiares de mi habitación."
    )

    print("")
    print(
        "Me aventuré fuera de mi santuario, con el corazón latiendo en mi garganta. Las escaleras crujieron bajo el peso de mi miedo mientras descendía hacia el reino de la incertidumbre. Un eco distorsionado de susurros y pasos invadía la casa, y cada sombra parecía albergar una amenaza oculta."
    )
    print("")
    print(
        "Al llegar al piso inferior, la realidad se reveló ante mí con brutalidad. Una penumbra extraña envolvía la sala de estar, y en la oscuridad, vi la figura de un intruso. Mis padres, antes guardianes de mi paz, yacían inertes en el suelo. El horror nacía en mi pecho mientras mi mente se resistía a aceptar la escena grotesca frente a mis ojos."
    )
    print("")
    print(
        "El intruso, un hombre enmascarado por las sombras, no tardó en notar mi presencia. Sus ojos, reflectores de malevolencia, se encontraron con los míos. No buscaban comprensión, solo codicia. En ese instante, la tragedia de la noche se reveló: mi familia, víctima de un destino retorcido, y yo, condenada a participar en una danza absurda de desesperación."
    )
    print("")
    print(
        "—Eres la pieza que completa mi juego —dijo el intruso con una calma escalofriante."
    )
    opcion1 = input("¿A qué juego se refiere el secuestrador?")
    return opcion1


def mostrar_parte_2():
    print(
        "Mis pasos resonaban en la penumbra, una coreografía silente que evitaba la atención de mi inesperado captor. Cada rincón de la casa se transformaba en una encrucijada de temores, y mi mente, atrapada en el absurdo de la situación, trataba de dar sentido a un mundo desprovisto de razón."
    )
    print("")
    print(
        "Cauta, me deslizaba por las sombras, con el latido de mi corazón resuenándome en los oídos, una banda sonora de terror que acompañaba mi danza furtiva. Cada habitación era un campo de batalla, y mis pasos, apenas un susurro en el escenario de esta tragedia absurda."
    )
    print("")
    print(
        "El secuestrador, una sombra amenazante, seguía mis movimientos con una paciencia que solo el existencialismo podría entender. ¿Qué sentido tenía esta persecución, este juego macabro de escondite en el teatro de una casa desgarrada por la violencia?"
    )
    print("")
    print(
        "Cada vez que creía haber encontrado un refugio seguro, el eco de sus pasos resonaba en mi conciencia, desafiando mi intento de escapar del sinsentido de la vida. La desesperación se filtraba en mi ser, como si el universo mismo se burlara de mi afán de escapar de un destino cruel e irracional."
    )
    print("")
    print(
        "Las lágrimas se confundían con el sudor en mi rostro mientras recorría los pasillos que antes eran mi refugio, ahora convertidos en corredores de desesperación. Mis pensamientos se entrelazaban con las sombras, creando una maraña de interrogantes que amenazaban con ahogar mi cordura."
    )
    print("")
    print(
        "En el umbral de la cocina, el escenario de nuestra danza infernal alcanzó su clímax. Mis espaldas contra la pared, y el secuestrador, una presencia siniestra, emergió de la oscuridad como el reflejo de un destino inevitable."
    )
    print("")
    print(
        "—¿Por qué huyes? —su voz, más un susurro que una pregunta, perforó el silencio—. ¿No entiendes que esta fuga es tan absurda como la existencia misma?"
    )
    print("")
    opcion2 = input("Tomas un objeto de la cocina ¿Qué tomas?")
    return opcion2


def mostrar_parte_3():
    print(
        "Mis ojos, reflejos de terror, se encontraron con los suyos. La cocina, una caja de resonancia para los suspiros existenciales, se convirtió en el epicentro de un diálogo entre dos almas perdidas en el caos del absurdo."
    )
    print("")
    print(
        "—Intento escapar de la sinrazón, de este juego sin reglas —respondí, mi voz apenas un susurro."
    )
    print("")
    print(
        "—¿Acaso no ves que la sinrazón nos abraza en cada esquina? La vida, un enigma sin solución, y nosotros, dos actores atrapados en un guion incomprensible."
    )
    print("")
    print(
        "La ironía del destino nos envolvía, dos seres condenados a danzar en el absurdo de la existencia. Mis ojos, ahora más allá del miedo, reflejaban una resignación forjada en el crisol de la desesperación."
    )
    print("")
    print(
        "—Somos prisioneros de un destino que no elegimos. ¿Acaso la libertad es solo una ilusión en este teatro trágico?"
    )
    print("")
    print(
        "El secuestrador, por un instante, pareció atrapado en una introspección profunda. La realidad, un enigma sin respuesta, se reflejaba en sus ojos vacíos."
    )
    print("")
    print(
        "—¿Qué sentido tiene esta búsqueda, este juego de gato y ratón? —preguntó, no a mí, sino al cosmos que se negaba a revelar sus secretos."
    )
    print("")
    print(
        "La cocina, testigo mudo de nuestras almas desnudas, se sumió en un silencio opresivo. El tiempo, como un compás desgastado, marcaba el ritmo de una verdad incómoda: nuestra lucha, una pequeña tragedia en un universo indiferente."
    )
    print("")
    print(
        "—¿Por qué resistes al absurdo de la vida? —lanzó el secuestrador su pregunta existencialista final."
    )
    print("")
    opcion3 = input("¿A qué parte de la casa vas a huir?")
    return opcion3


def mostrar_parte_4():
    print("")
    print(
        "Cada paso que daba resonaba en la caverna de mi miedo. La decisión de huir, un acto de desesperación, me llevó a los recovecos más oscuros de la casa, como una sombra danzante en un ballet macabro. El secuestrador seguía mis huellas, una presencia imparable en este juego absurdo de escapar del destino."
    )
    print("")
    print(
        "En mi huida, tropecé con el teléfono de mi hermano. Mis manos temblorosas se aferraron al aparato como a un salvavidas en un océano de terror. Marcar el número de emergencia se convirtió en un acto de resistencia, una última esperanza en un mundo donde la desesperanza reinaba."
    )
    print("")
    print(
        "El tono de llamada resonaba en mis oídos, una melodía de socorro que contrastaba con la cacofonía del peligro. Mis dedos tambalearon sobre las teclas, marcando los dígitos que podrían ser mi salvación. Pero justo cuando la conexión parecía establecerse, el secuestrador se abalanzó sobre mí, su sombra eclipsando cualquier esperanza de ayuda."
    )
    print("")
    print(
        "Con mano cruel, arrebató el teléfono de mis manos, y con la otra, tapó mi boca. El universo entero pareció colapsar en ese instante, mi aliento atrapado entre sus dedos como una mariposa presa de una red mortal."
    )
    print(
        "El secuestrador, con su voz susurrante, se apoderó de la conversación. Mi intento de gritar quedó sofocado por su agarre implacable. Escuché solo fragmentos distorsionados de su diálogo con la policía, una pesadilla sonora que pintaba un cuadro escalofriante de mi desesperación."
    )
    print("")
    print(
        "—No te preocupes, oficial, es solo un malentendido. La niña está bien... —sus palabras, una mentira macabra, se filtraban a través de mis labios sellados.—No te preocupes, oficial, es solo un malentendido. La niña está bien... —sus palabras, una mentira macabra, se filtraban a través de mis labios sellados."
    )
    print("")
    print(
        "—No te preocupes, oficial, es solo un malentendido. La niña está bien... —sus palabras, una mentira macabra, se filtraban a través de mis labios sellados."
    )
    print("")
    print(
        "Las lágrimas se mezclaban con el miedo en mis ojos mientras el secuestrador tejía su red de engaños. La policía, ajena a mi tragedia, se convertía en cómplice involuntaria de mi condena."
    )
    print("")
    print(
        "—Sí, sí, la dejaré hablar... —mi voz, un eco apagado, apenas se filtraba en la conversación manipulada—. Solo asegúrate de enviar a alguien rápido"
    )
    print("")
    print(
        "Mis súplicas silenciadas se ahogaban en la frialdad de sus manos, y la llamada que debería haber sido mi salvación se convirtió en una herramienta en su malévolo juego. La policía, ciega ante el teatro macabro, se retiraría, y yo, una marioneta en sus manos, seguiría danzando en el absurdo de mi destino."
    )
    print("")
    print(
        "El secuestrador, al colgar, dejó un rastro de susurros ominosos que flotaron en el aire cargado de desesperación. La llamada, una ilusión de esperanza, se desvaneció en el viento de mi desdicha, y en la penumbra de mi prisión, solo quedaba el eco de mi propio silencio roto."
    )
    print("")
    opcion4 = input(
        "El secuestrador te pregunta por tu comida favorita ¿Qué respondes?"
    )
    print("")
    return opcion4


def mostrar_parte_5():
    print("")
    print(
        "El secuestrador, en lugar de mostrar compasión o desprecio, soltó una risa siniestra que reverberó en el silencio pesado de la habitación. Su risa, un eco de desprecio por la fragilidad de mi existencia, me heló hasta los huesos."
    )
    print("")
    print(
        "La risa del secuestrador era como un eco en mi mente, una sinfonía de locura que resonaba en cada rincón de la casa. Intenté escapar de esa risa, pero cada paso era un eco de su burla, un recordatorio constante de mi vulnerabilidad."
    )
    print("")
    print(
        "Desesperada, corrí hacia el cuarto de mis padres, donde la sombra de mi padre se extendía sobre el armario. Abrí la puerta con manos temblorosas y mis ojos se encontraron con la escopeta de mi padre, una reliquia de tiempos más seguros."
    )
    print("")
    print(
        "La tomé con determinación, sintiendo el peso de la responsabilidad en mis manos. Al regresar a la sala, la escopeta sostenida con firmeza, apunté al secuestrador. Su risa se desvaneció por un momento, reemplazada por un silencio tenso."
    )
    print("")
    print(
        "—No te acerques. —mi voz, ahora imbuida de un coraje inesperado, resonó en la sala"
    )
    print("")
    print(
        "El secuestrador, en un giro teatral, alzó las manos en señal de rendición. Sin embargo, sus ojos brillaban con una chispa de malicia, y su risa resurgió, estridente y cruel."
    )
    print("")
    print(
        "—¿Crees que eso te salvará? ¿Crees que puedes enfrentarte a mí con esa triste utilería? —su risa, como cuchillas en la oscuridad, cortaba mi valentía recién encontrada."
    )
    print("")
    print(
        "Mis ojos se encontraron con el cañón de la escopeta, y una verdad brutal se reveló: la escopeta de mi padre, una reliquia de protección, era solo una réplica inofensiva. El secuestrador, al darse cuenta de mi engaño, rió con una sátira que resonaba en las paredes."
    )
    print("")
    print(
        "—¿De verdad pensaste que podrías desafiar la absurda realidad con un juguete? Qué ingenua eres, pequeña. —su risa, como un canto de derrota, me envolvió en la cruel realidad de mi impotencia."
    )
    print("")
    print(
        "La escopeta de utilería se volvió un símbolo grotesco de mi desesperación, y el secuestrador, el maestro de la farsa, disfrutaba del drama de mi tragedia. La risa persistía, un eco que se mezclaba con mi llanto silencioso mientras enfrentaba la absurda ironía de mi propia farsa."
    )
    opcion5 = input("¿Ahora qué haces?.")
    return opcion5


def mostrar_parte_6():
    print("")
    print(
        "El sonido hueco de los nudillos golpeando la puerta reverberó en la sala, interrumpiendo la sinfonía macabra de la risa del secuestrador. El vigilante del fraccionamiento, un intruso inadvertido en nuestra pesadilla, había detectado la disonancia en la tranquilidad nocturna. Un destello de alivio iluminó mis ojos, aunque efímero, ante la posibilidad de ayuda."
    )
    print("")
    print(
        "Sin embargo, la frágil esperanza se disipó cuando el secuestrador, una sombra que se movía con sigilo, se acercó a mí con un rollo de cinta de aislar en sus manos. Sus ojos, dos abismos oscuros, reflejaban la malevolencia de su plan mientras mis manos eran hábilmente inmovilizadas."
    )
    print("")
    print(
        "La cinta de aislar, un símbolo de mi impotencia, rodeó mis muñecas con la frialdad de la traición. El secuestrador, indiferente a mis súplicas ahogadas, me condujo hacia el armario donde momentos antes había buscado refugio. La puerta se cerró con un chirrido, dejándome atrapada en la oscuridad claustrofóbica."
    )
    print("")
    print(
        "El secuestrador, con la despiadada eficiencia de un carcelero, aseguró la cinta alrededor del armario, sellando mi destino en aquel ataúd improvisado. Mi corazón, un tambor en el silencio opresivo, marcaba el ritmo de mi desesperación."
    )
    print("")
    print(
        "El toque persistente en la puerta continuaba, ajeno al drama interno que se desarrollaba en las sombras. El secuestrador, con una calma que revelaba su maestría en el engaño, se dirigió hacia la entrada para recibir al inquisitivo vigilante."
    )
    print("")
    print(
        "Desde mi prisión de madera y oscuridad, escuché los murmullos distorsionados, una conversación que se perdía en el viento de la noche. Mi esperanza, un hilo endeble, se deshilachaba con cada segundo que pasaba."
    )
    print("")
    print(
        "De repente, un estruendo amortiguado rompió la tranquilidad. Un choque sordo, como el lamento de un pájaro herido, resonó en la casa. El secuestrador, el maestro de la farsa, había desplegado su teatro oscuro una vez más."
    )
    print("")
    print(
        "La puerta del armario se abrió con una luz que se coló desde el exterior, y vi al secuestrador de pie, una figura enigmática, su sombra proyectada sobre mi encierro. Mis ojos, ansiosos de comprender el desenlace, se encontraron con los suyos, ahora teñidos de triunfo sádico."
    )
    print("")
    print(
        "—El teatro continúa, pequeña. —su voz, una sinfonía de desdén, resonó en el vacío—. El vigilante ha sido silenciado, y tú, una marioneta en mi obra maestra absurda."
    )
    print("")
    print(
        "La cinta de aislar, un lazo que me mantenía prisionera, se desenredó con la gracia de un verdugo consumado. El secuestrador, con una sonrisa que destilaba la amargura del destino, cerró la puerta del armario, dejándome en la penumbra de mi encierro mientras el telón caía en el acto oscuro de esta tragedia absurda."
    )
    opcion6 = input("¿Con qué arma noqueó el secuestrador al vigilante?.")
    return opcion6


def mostrar_parte_7():
    print("")
    print(
        "La cinta de aislar seguía apretada en mis muñecas mientras era transportada en la caja de la camioneta, inmovilizada por el frío metal. La oscuridad abrazaba mi pequeño refugio, y la única compañía era el murmullo constante de los pensamientos en mi mente atormentada."
    )
    print("")
    print(
        "El secuestrador, en el asiento delantero, lanzó un discurso que resonó en la caja como un eco de desesperación. Habló de su deseo de liberarse de las cadenas del trabajo, de la búsqueda insaciable de comodidad y lujo que el dinero proporcionaría. Sus palabras, tintadas con un existencialismo retorcido, se deslizaban entre las rendijas de mi prisión improvisada."
    )
    print("")
    print(
        "—Nunca he entendido el sentido de trabajar toda una vida para sobrevivir —declaró con una amargura que cortaba como cuchillas—. El dinero, un puente hacia la libertad de la monotonía. La sociedad, una cárcel que nos somete a la rutina sin sentido."
    )
    print("")
    print(
        "Su voz, un susurro intrusivo, pintaba un cuadro de su propia desdicha mientras yo, una pieza involuntaria de su rompecabezas, escuchaba atenta. La camioneta avanzaba por calles oscuras y solitarias, y las palabras del secuestrador flotaban en el aire denso como un perfume intoxicante."
    )
    print("")
    print(
        "-El abuelo de la niña, el magnate adinerado, representa el medio para mi liberación. El dinero que posee es mi boleto hacia una vida sin esfuerzo, una existencia desprovista de las cadenas del trabajo —explicó, su voz resonando con un fervor absurdo—. Todos somos esclavos de nuestras circunstancias, y yo, simplemente, busco cambiar las mías."
    )
    print("")
    print(
        "Cada palabra era una losa en mi conciencia, un recordatorio punzante de mi posición en este juego macabro. La camioneta se movía con una inevitable determinación, llevándome hacia un destino incierto que el secuestrador planeaba moldear a su antojo."
    )
    print("")
    print(
        "Sin embargo, en medio de su discurso existencialista, un sonido metálico surgió de la camioneta. Una vibración inquietante, como un lamento mecánico, resonó en la caja. Mis oídos, atentos a cada susurro de la noche, captaron la anormalidad en el rugir del motor."
    )
    print("")
    print(
        "El secuestrador, ajeno al giro inesperado de los acontecimientos, continuó con su monólogo mientras la camioneta parecía luchar contra algún inconveniente mecánico. Una paleta de emociones se pintó en mi rostro, una mezcla de intriga y temor, mientras me preguntaba: ¿qué va mal en la camioneta?"
    )
    print("")
    opcion7 = input(
        "El inminente desenlace, marcado por un problema desconocido en la maquinaria de nuestra tragedia compartida, dejó en el aire una pregunta que flotaba como una sombra ominosa: ¿qué va mal en la camioneta?."
    )
    return opcion7


def mostrar_parte_8():
    print("")
    print(
        "El secuestrador, en medio de su monólogo existencial, sintió la repentina parálisis de la camioneta. El rugido del motor cesó, sumiendo la escena en un silencio inquietante. A regañadientes, se vio obligado a detenerse, abandonando sus delirios de libertad sin esfuerzo."
    )
    print("")
    print(
        "Con una expresión de frustración, el secuestrador se bajó de la camioneta y abrió el capó, sumergiéndose en una revisión apresurada. Mis ojos, desde mi prisión forzada en la caja, observaban con cautela mientras él intentaba descifrar el misterio mecánico."
    )
    print("")
    print(
        "En la penumbra de la noche, sin que el secuestrador lo notara, las luces intermitentes de una patrulla de la Guardia Nacional se acercaban sigilosamente. Las sombras de los guardianes de la ley se deslizaban entre los árboles cercanos, envueltos en la oscuridad como fantasmas del orden."
    )
    print("")
    print(
        "El comandante de la Guardia Nacional, un hombre de semblante severo pero ojos perspicaces, se acercó al secuestrador mientras este intentaba resolver el enigma del motor apagado. El diálogo se desarrolló en susurros, como conspiradores en una tragedia compartida."
    )
    print("")
    print(
        "—¿Problemas mecánicos? —preguntó el comandante con una frialdad que contradecía la gravedad de la situación."
    )
    print("")
    print(
        "—Sí, parece ser un contratiempo inoportuno —respondió el secuestrador, su voz tratando de ocultar la inquietud."
    )
    print("")
    print(
        "La Guardia Nacional, astuta en su observación, no tardó en notar el rastro de mi presencia en la camioneta. El comandante, con mirada aguda, intuyó la discrepancia entre la apariencia de una camioneta común y el sutil indicio de una tragedia oculta."
    )
    print("")
    print(
        "—¿Puedo revisar el vehículo? —inquirió el comandante, sus ojos escudriñando la escena en busca de respuestas."
    )
    print("")
    print(
        "El secuestrador, forzado por las circunstancias, asintió con una renuencia apenas disimulada. La caja de la camioneta se abrió, revelando mi presencia, una víctima de circunstancias más allá de mi control. El comandante, con un gesto de autoridad, ordenó la liberación de mis ataduras."
    )
    print("")
    print(
        "La verdad, ese oscuro secreto encerrado en la caja, emergió como un suspiro agónico en la fría noche. La Guardia Nacional, encargada de salvaguardar la justicia, enfrentó la realidad de una historia macabra tejida en la trama de mi existencia."
    )
    print("")
    opcion8 = input(
        "¿Qué adjetivo calificativo usó el secuestrador para referirse al comandante que hio que se detuviera?"
    )
    return opcion8


def mostrar_parte_9():
    print("")
    print(
        "El comandante de la Guardia Nacional, rostro endurecido por años de servicio, no dudó en aplicar una justicia implacable al secuestrador. Sus puños eran martillos que golpeaban la máscara del mal que había amenazado mi existencia. Cada golpe resonaba como un eco de retribución en la desolada noche del desierto."
    )
    print("")
    print(
        "El secuestrador, en un intento desesperado por escapar del torrente de justicia, se vio obligado a correr hacia la oscuridad implacable del desierto. Sus pasos, un repiqueteo frenético en la arena, apenas le otorgaban una frágil ventaja contra el comandante decidido a impartir un castigo acorde con la gravedad de sus acciones."
    )
    print("")
    print(
        "La luna, testigo mudo de la tragedia que se desarrollaba en su teatro nocturno, iluminaba la desesperada huida del secuestrador. La vastedad del desierto, un escenario sin límites, parecía cerrar sus puertas en un intento de atrapar al fugitivo en un abrazo sin escape."
    )
    print("")
    print(
        "Desde la distancia, los disparos resonaban como truenos, la simetría caótica de una batalla en medio de la nada. La niña, liberada de su prisión y testigo de esta epopeya sombría, imaginaba la danza mortífera en la penumbra del desierto."
    )
    print("")
    print(
        "El eco de las detonaciones reverberaba en la oscuridad, cada disparo una balada de violencia y desesperación. El secuestrador, perdido en la vastedad del desierto, respondía con tiros erráticos, un lamento desesperado contra la sentencia que se cernía sobre él."
    )
    print("")
    print(
        "La niña, con ojos abiertos a lo desconocido, visualizaba la escena con una mezcla de horror y asombro. El secuestrador, una figura fugaz en la inmensidad de la noche, se volvía un espectro en la danza mortal que se desplegaba ante sus ojos."
    )
    print("")
    print(
        "Los disparos resonaron hasta que el silencio, más oscuro que cualquier sombra, se adueñó del desierto. El comandante, un implacable juez en esta tragedia, emergió del vacío portando la certeza de la justicia cumplida."
    )
    print("")
    print(
        "La niña, atrapada en el teatro macabro, intentaba asimilar el epílogo de esta historia en el desierto. La luna, ahora testigo de la derrota del mal, derramaba su luz sobre la escena final. La vastedad del desierto, silente y eterna, absorbía el suspiro de la batalla, dejando tras de sí una huella indeleble en el lienzo infinito del horizonte."
    )
    print("")
    opcion9 = input("¿De qué color se pintó el cielo esa noche?")
    return opcion9


def final_bueno():
    print(
        "Un suspiro tembloroso escapó de mis labios mientras mis ojos se abrían al mundo. La realidad, con su luz matinal suave, se filtraba en mi habitación, disipando las sombras de la pesadilla que había sido mi sueño. El eco de la batalla en el desierto, los disparos y la persecución, se desvanecieron como el humo de un sueño que se desliza entre los dedos al despertar."
    )
    print("")
    print(
        "Mis manos, antes atadas por la cinta de aislar, se encontraban libres, una evidencia tangible de que la opresión que había experimentado no era más que una construcción onírica. El peso del secuestrador, el comandante y el desierto se desvanecieron, dejando solo el eco de un relato surrealista que ahora yacía en el rincón borroso de mis recuerdos."
    )
    print("")
    print(
        "Mis ojos exploraron la habitación familiar, los detalles familiares volvían a cobrar sentido, y la sensación de libertad inundó mi ser como una ola de alivio. La luna, testigo de la noche ficticia, se disolvía en la luz del día, y el mundo real recuperaba su color y forma."
    )
    print("")
    print(
        "Fue entonces cuando entendí que todo había sido un sueño, una trama intrincada tejida por la imaginación mientras mi mente exploraba los rincones más oscuros de la realidad. El secuestrador, el comandante, la batalla en el desierto, cada elemento se desmoronaba como un castillo de naipes al amanecer."
    )
    print("")
    print(
        "Me incorporé en la cama, sopesando la dualidad de la experiencia, la delirante intensidad de la pesadilla y la serenidad de la vigilia recién recuperada. El alivio se mezclaba con la extrañeza, como si hubiera emergido de un viaje en el que los límites entre la realidad y la fantasía se habían desdibujado."
    )
    print("")
    print(
        "Aunque mi corazón aún latía con la impresión de la pesadilla, la certeza de que todo era un sueño me abrazaba con la dulzura de la realidad restaurada. Mis pensamientos, antes atrapados en la telaraña del absurdo, se liberaron hacia la claridad del día que se extendía más allá de mi ventana."
    )
    print("")
    print(
        "Así, con un suspiro de alivio y una sonrisa de incredulidad, me sumergí en el mundo despierto, agradeciendo que la única verdad inquebrantable era la luz del día y la certeza reconfortante de que todo había sido un sueño, un viaje onírico que ahora quedaba atrás mientras abrazaba la cotidianidad de la vigilia."
    )


def final_medio():
    print("")
    print(
        "Un temblor recorrió mi cuerpo mientras abría los ojos, solo para encontrarme con la oscura realidad de la cajuela de una camioneta. La sensación de confinamiento, aunque menos intensa que en el sueño, persistía como un eco molesto. Sin embargo, esta vez, mis manos no estaban atadas, y la certeza de que era más que un sueño pesadillesco empezó a consolidarse."
    )
    print("")
    print(
        "Un sonido metálico resonó en la penumbra, y la puerta de la cajuela se abrió con un chirrido agudo. La luz del día se coló, despejando las sombras y revelando la figura del comandante de la Guardia Nacional. Su mirada, ahora real y llena de determinación, encontró la mía con un destello de compasión."
    )
    print("")
    print(
        "—Estás a salvo ahora. —sus palabras, un susurro reconfortante, disolvieron el último vestigio de la pesadilla que había marcado mi descanso."
    )
    print("")
    print(
        "Mis piernas, entumecidas por el confinamiento, encontraron firmeza en el suelo mientras el comandante extendía su mano. Me ayudó a salir de la cajuela, liberándome de la prisión ficticia que había albergado mis miedos más oscuros."
    )
    print("")
    print(
        "La camioneta, ahora inmóvil y desprovista de la sombra del secuestrador, era un testigo silente de la intervención providencial de la Guardia Nacional. Las huellas de la batalla onírica se desvanecieron, y el sol del día real acarició mi rostro, otorgándome una sensación tangible de libertad."
    )
    print("")
    print(
        "—Gracias. —mis palabras, cargadas de gratitud, apenas lograron expresar la magnitud de lo que sentía."
    )
    print("")
    print(
        "El comandante asintió con una sonrisa serena, como un protector que había cumplido con su deber. Mi rescate, un acto tangible en el escenario de la realidad, se convirtió en el epílogo redentor de una historia que, aunque nacida en los confines de la imaginación, encontró su conclusión en la luz del día."
    )
    print("")
    print(
        "La Guardia Nacional, con su presencia imponente, representó la promesa cumplida de la seguridad y la justicia. La camioneta, antes un vehículo de pesadilla, se transformó en el símbolo de una amenaza que fue enfrentada y superada."
    )
    print("")
    print(
        "Así, de la cajuela de la camioneta al abrazo de la libertad, dejé atrás los restos del sueño oscuro. El comandante, mi salvador real, se convirtió en un faro que guió mi regreso a la realidad. Y mientras la camioneta quedaba atrás, una reliquia inmóvil de una trama onírica, yo avanzaba hacia el día que se extendía ante mí, agradecida por la intervención que había llevado el alivio a la frontera entre el sueño y la vigilia."
    )


def final_malo():
    print(
        "Mis ojos se abrieron con dificultad, y una sensación punzante me recordó que aún estaba en la cajuela de la camioneta. La oscuridad persistía, pero esta vez no había alivio al despertar. Un dolor agudo, como el filo de un cuchillo, me recorría el cuerpo. Al palpar mi abdomen, mis dedos se tiñeron de rojo oscuro."
    )
    print("")
    print(
        "La bala perdida, una sombra en la noche de mi destino, había encontrado su camino hacia una arteria vital. Sentía la vida escapándose de mí, un río que se deslizaba silenciosamente hacia la oscuridad. Cada latido, antes un eco de esperanza, se volvía un recordatorio implacable de mi inevitable destino."
    )
    print("")
    print(
        "La cajuela, antes una prisión ficticia, se volvía mi refugio final. Cada respiración se volvía un suspiro melancólico mientras la realidad se desdibujaba en el velo de la muerte. La luz del día, un testigo indiferente, apenas filtraba la penumbra de mi despedida."
    )
    print("")
    print(
        "Fue entonces cuando la puerta de la cajuela se abrió con un chirrido. La luz, fría y distante, acarició mi rostro mientras la figura del comandante de la Guardia Nacional se inclinaba hacia mí. Su expresión pasó de la determinación a la consternación al percatarse de la tragedia que se desarrollaba ante sus ojos."
    )
    print("")
    print(
        "—Lo siento… —sus palabras, apenas un susurro, se perdieron en el viento triste de la tarde."
    )
    print("")
    print(
        "La realidad, cruda y despiadada, se desplegó ante mis ojos mientras los esfuerzos de la Guardia Nacional para salvarme se volvían un eco lejano. Mis pensamientos se deslizaban hacia la penumbra mientras mi cuerpo se sumía en el abrazo frío de la muerte."
    )
    print("")
    print(
        "La cajuela se cerró, un ataúd improvisado que contenía la tragedia final. El sonido de la Guardia Nacional, una sinfonía de impotencia, se desvaneció en la distancia. Mi conciencia, como una vela que parpadea por última vez, se extinguía lentamente."
    )
    print("")
    print(
        "Así, entre sombras y susurros de despedida, me despedía de un mundo que, aunque nacido en la imaginación, encontraba su conclusión en la cruel realidad. La niña, cuya existencia había sido un lienzo tejido con los hilos de la tragedia, se desvanecía en la eternidad, llevándose consigo la última nota de una historia que nunca encontraría su resolución"
    )


def juego():
    mostrar_ascii_art()

    opcion1 = mostrar_intro()
    opcion2 = mostrar_parte_2()
    opcion3 = mostrar_parte_3()
    opcion4 = mostrar_parte_4()
    opcion5 = mostrar_parte_5()
    opcion6 = mostrar_parte_6()
    opcion7 = mostrar_parte_7()
    opcion8 = mostrar_parte_8()
    opcion9 = mostrar_parte_9()
    seleccion = []
    seleccion.append(opcion1)
    seleccion.append(opcion2)
    seleccion.append(opcion3)
    seleccion.append(opcion4)
    seleccion.append(opcion5)
    seleccion.append(opcion6)
    seleccion.append(opcion7)
    seleccion.append(opcion8)
    seleccion.append(opcion9)

    elementos = [
        # Juegos
        "ajedrez",
        "dominó",
        "jenga",
        "parchís",
        "damas",
        "monopoly",
        "scrabble",
        "catan",
        "risk",
        "trivial",
        "póker",
        "ludo",
        "battleship",
        "connect 4",
        "twister",
        "backgammon",
        "carcassonne",
        "uno",
        "yahtzee",
        "clue",
        "chutes and ladders",
        "bingo",
        "go",
        "chess",
        "checkers",
        "mahjong",
        "card games",
        "video games",
        # Utensilios de cocina
        "cuchillo",
        "tenedor",
        "cuchara",
        "sartén",
        "olla",
        "cucharón",
        "espátula",
        "cucharilla",
        "pelador",
        "tabla de cortar",
        "batidor",
        "colador",
        "molde para pastel",
        "rallador",
        "exprimidor",
        "taza de medir",
        "rodillo",
        "termómetro de cocina",
        "báscula",
        "abrelatas",
        "tijeras de cocina",
        "molinillo de pimienta",
        # Lugares de una casa
        "dormitorio",
        "sala de estar",
        "cocina",
        "baño",
        "comedor",
        "despensa",
        "estudio",
        "sótano",
        "ático",
        "garaje",
        "vestíbulo",
        "terraza",
        "jardín",
        "armario",
        "desván",
        "cuarto de lavado",
        "biblioteca",
        "gimnasio",
        "cuarto de juegos",
        "sala de cine",
        "habitación de invitados",
        "taller",
        "cuarto de música",
        # Platillos
        "pizza",
        "sushi",
        "lasagna",
        "enchiladas",
        "hamburguesa",
        "curry",
        "tacos",
        "pasta alfredo",
        "ceviche",
        "paella",
        "ramen",
        "bistec a la parrilla",
        "pollo al curry",
        "sopa de tomate",
        "pastel de chocolate",
        "helado",
        "ensalada césar",
        "spaghetti bolognese",
        "sándwich de pollo",
        "pescado a la parrilla",
        "sopa de lentejas",
        "quesadillas",
        "tarta de manzana",
        "sopa de fideos de huevo",
        "camarones a la parrilla",
        "arroz frito",
        "rollitos de primavera",
        "tortilla española",
        "tiramisú",
        "goulash",
        "barbacoa",
        "cordero asado",
        # Verbos en presente
        "jugar",
        "cocinar",
        "estudiar",
        "correr",
        "saltar",
        "leer",
        "escribir",
        "hablar",
        "bailar",
        "nadar",
        "cantar",
        "reír",
        "dormir",
        "comer",
        "beber",
        "trabajar",
        "descansar",
        "observar",
        "explorar",
        "crear",
        "escuchar",
        "pensar",
        "amar",
        "soñar",
        "vivir",
        "construir",
        "aprender",
        "enseñar",
        "resolver",
        "viajar",
        "despertar",
        "conversar",
        "disfrutar",
        "correr",
        "caminar",
        "abrazar",
        "cuidar",
        "compartir",
        "celebrar",
        "ayudar",
        "imaginar",
        "innovar",
        "saltar",
        "dibujar",
        "viajar",
        "viajar",
        "mirar",
        "gastar",
        "encontrar",
        # Elementos de una camioneta
        "volante",
        "asientos",
        "espejo retrovisor",
        "palanca de cambios",
        "freno de mano",
        "radio",
        "aire acondicionado",
        "llaves",
        "parabrisas",
        "limpiaparabrisas",
        "maletero",
        "luces",
        "neumáticos",
        "tapacubos",
        "cinturones de seguridad",
        "caja de herramientas",
        "gato hidráulico",
        "triángulos de emergencia",
        "llanta de repuesto",
        "batería",
        "aceite del motor",
        "radiador",
        "filtro de aire",
        "filtro de aceite",
        "freno",
        "embrague",
        "alternador",
        "correa de transmisión",
        "amortiguadores",
        # Adjetivos calificativos
        "espléndido",
        "aventurero",
        "elegante",
        "luminoso",
        "delicioso",
        "majestuoso",
        "brillante",
        "emocionante",
        "innovador",
        "fresco",
        "colorido",
        "exquisito",
        "divertido",
        "relajante",
        "creativo",
        "armonioso",
        "cautivador",
        "fascinante",
        "pintoresco",
        "acogedor",
        "apasionante",
        "sorprendente",
        "impresionante",
        "festivo",
        "festivo",
        "intenso",
        "cálido",
        "fragante",
        "extraordinario",
        "refrescante",
        "tranquilo",
        "rojo",
        "azul",
        "amarillo",
        "verde",
        "naranja",
        "morado",
        "rosa",
        "negro",
        "blanco",
        "gris",
        "marrón",
        "beige",
        "celeste",
        "turquesa",
        "cian",
        "índigo",
        "violeta",
        "ocre",
        "coral",
        "salmon",
        "terracota",
        "lavanda",
        "marfil",
        "esmeralda",
        "rubí",
        "zafiro",
        "ámbar",
        "aqua",
        "lila",
        "gris perla",
        "carmesí",
        "dorado",
        "plateado",
        "melocotón",
        "azafrán",
        "púrpura",
        "café",
        "oliva",
        "almendra",
        "cobre",
        "ciruela",
        "gris marengo",
        "mostaza",
        "granate",
        "caqui",
        "pistacho",
        "ámbar",
        "malva",
        "fucsia",
        "bronce",
        "orquídea",
        "azul marino",
        "salvia",
        "perla",
        "ceniza",
        "bermellón",
        "coralino",
        "turmalina",
        "rosa pastel",
        "lima",
        "champán",
        "índigo",
        "gris oscuro",
        "azul cielo",
        "sepia",
        "borgoña",
        "azul eléctrico",
        "ocre amarillo",
        "blanco antiguo",
        "rojo bermellón",
        "gris pizarra",
        "amarillo canario",
        "verde manzana",
        "rubor",
        "canela",
        "rosa chicle",
        "topacio",
        "rojo burdeos",
        "azul cobalto",
        "berilo",
        "gris azulado",
        "magenta",
        "gris plomo",
        "rosa mexicano",
        "azul cerúleo",
        "gris lobo",
        "rojo coral",
        "verde oliva",
        "blanco hueso",
        "rojo púrpura",
        "azul real",
        "amarillo limón",
        "verde menta",
        "rojo borgoña",
        "cobre rojo",
        "azul zafiro",
        "blanco marfil",
        "rojo oscuro",
        "azul ultramar",
        "amarillo oro",
        "rosa fuerte",
        "gris cemento",
        "verde jade",
        "naranja oscuro",
        "rosa oscuro",
        "amarillo oro viejo",
        "azul claro",
        "amarillo lima",
        "marrón claro",
        "verde pistacho",
        "rosa claro",
        "lila claro",
        "gris claro",
        "verde claro",
        "naranja claro",
        "azul claro",
        "amarillo claro",
        "rojo claro",
        "morado claro",
        "rosa claro",
        "gris claro",
        "verde claro",
        "naranja claro",
        "azul claro",
        "amarillo claro",
        "rojo claro",
        "morado claro",
    ]
    diccionario_elementos = {elemento: random.randint(1, 3) for elemento in elementos}
    contador_de_puntos = 0

    if opcion1.lower() in diccionario_elementos:
        contador_de_puntos += diccionario_elementos[opcion1.lower()]
    if opcion2.lower() in diccionario_elementos:
        contador_de_puntos += diccionario_elementos[opcion2.lower()]
    if opcion3.lower() in diccionario_elementos:
        contador_de_puntos += diccionario_elementos[opcion3.lower()]
    if opcion4.lower() in diccionario_elementos:
        contador_de_puntos += diccionario_elementos[opcion4.lower()]
    if opcion5.lower() in diccionario_elementos:
        contador_de_puntos += diccionario_elementos[opcion5.lower()]
    if opcion6.lower() in diccionario_elementos:
        contador_de_puntos += diccionario_elementos[opcion6.lower()]
    if opcion7.lower() in diccionario_elementos:
        contador_de_puntos += diccionario_elementos[opcion7.lower()]
    if opcion8.lower() in diccionario_elementos:
        contador_de_puntos += diccionario_elementos[opcion8.lower()]
    if opcion9.lower() in diccionario_elementos:
        contador_de_puntos += diccionario_elementos[opcion9.lower()]

    if contador_de_puntos < 10:
        final_malo()
    elif contador_de_puntos < 20:
        final_medio()
    else:
        final_bueno()
    
if __name__ == "__main__":
        juego()