"""Genera las páginas internas de ACP (comparten head, header, menú, footer y flotante).
Volver a correr después de cualquier cambio de estructura; el CSS va en styles.css.
El index está escrito a mano: si cambia el header o el footer, actualizarlo también ahí."""
import os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(D)

WA = "Hola, quisiera hacer una consulta."
FONTS = "https://fonts.googleapis.com/css2?family=Gilda+Display&family=Urbanist:wght@300;400;500;600;700&display=swap"
NAV = [("El estudio", "estudio.html"), ("Contable", "servicios-contables.html"), ("Sociedades", "servicios-contables.html#sociedades"),
       ("Jurídico", "servicios-juridicos.html"), ("Contacto", "index.html#contacto")]
CUR = ' aria-current="page"'
PX = {"columnas": 36857676, "fachada": 13219418, "libros": 1333742, "firma": 8730998, "congreso": 36699719}

def head(title, desc, robots=None):
    rb = f'<meta name="robots" content="{robots}">\n' if robots else ""
    return f'''<!DOCTYPE html>
<html lang="es-AR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{rb}<meta name="theme-color" content="#0E0C0B">
<link rel="icon" type="image/png" href="./favicon.png">
<link rel="apple-touch-icon" href="./favicon.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_AR">
<meta property="og:site_name" content="ACP Estudio Jurídico Contable">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="./og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="1200">
<meta name="twitter:card" content="summary">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.46.0/dist/tabler-icons.min.css">
<link rel="stylesheet" href="./styles.css">
</head>
<body>
'''

def header(active=None):
    links = "\n".join(f'      <a href="./{h}"{CUR if h == active else ""}>{t}</a>' for t, h in NAV)
    return f'''
<!-- ============ HEADER ============ -->
<header class="hdr" id="hdr">
  <div class="wrap hdr-in">
    <a href="./index.html" class="brand" aria-label="ACP Estudio Jurídico Contable, inicio">
      <img src="./logo-claro.png" alt="ACP Jurídico Contable" width="1179" height="648">
    </a>
    <nav class="nav" aria-label="Principal">
{links}
    </nav>
    <a class="btn btn-bordo btn-sm hdr-cta js-wa" href="#" data-msg="{WA}">Consultar</a>
    <button class="burger" id="burger" aria-label="Abrir menú" aria-controls="mnav" aria-expanded="false"><span></span><span></span></button>
  </div>
</header>

<div class="mnav-ov" id="mnavOv"></div>
<nav class="mnav" id="mnav" aria-label="Menú">
  <img src="./logo-claro.png" alt="" class="mnav-logo" width="1179" height="648">
{links.replace("      <a", "  <a")}
  <a class="btn btn-bordo js-wa" href="#" data-msg="{WA}">Consultar por WhatsApp</a>
</nav>
'''

FOOTER = f'''
<!-- ============ FOOTER ============ -->
<footer class="ftr" id="ftr">
  <div class="wrap ftr-in">
    <div class="ftr-brand">
      <img src="./logo-claro.png" alt="ACP Jurídico Contable" width="1179" height="648" loading="lazy">
      <p>Asesoramiento contable, impositivo y jurídico para personas, emprendedores y empresas del AMBA, desde 2012.</p>
    </div>
    <div class="ftr-col">
      <h4>Estudio</h4>
      <ul>
        <li><a href="./estudio.html">El estudio</a></li>
        <li><a href="./servicios-juridicos.html#trayectoria">Trayectoria</a></li>
        <li><a href="./index.html#contacto">Contacto</a></li>
      </ul>
    </div>
    <div class="ftr-col">
      <h4>Servicios</h4>
      <ul>
        <li><a href="./servicios-contables.html">Impuestos y monotributo</a></li>
        <li><a href="./servicios-contables.html#sueldos">Sueldos y RR. HH.</a></li>
        <li><a href="./servicios-contables.html#sociedades">Sociedades comerciales</a></li>
        <li><a href="./servicios-juridicos.html">Litigios y mediación</a></li>
      </ul>
    </div>
    <div class="ftr-col">
      <h4>Contacto</h4>
      <ul class="ftr-data">
        <li><i class="ti ti-brand-whatsapp"></i><a class="js-wa" href="#" data-msg="{WA}">11 5760-7128</a></li>
        <li><i class="ti ti-mail"></i><a href="mailto:acalderaro@acpestudio.com.ar">acalderaro@acpestudio.com.ar</a></li>
        <li><i class="ti ti-map-pin"></i><span>Av. Entre Ríos 1243, CABA</span></li>
      </ul>
    </div>
  </div>
  <div class="ftr-legal">
    <p>Gabriel Álvarez (Contador) C.P.C.E.C.A.B.A. T° 390 F° 26 y Adrián Calderaro Papa (Abogado) C.P.A.C.F. T° 113 F° 31.</p>
    <p>No somos una asociación de profesionales.</p>
  </div>
  <div class="ftr-bottom">
    <p>© <span id="yr">2026</span> ACP Estudio Jurídico Contable. Todos los derechos reservados.</p>
    <p><a href="./privacidad.html">Política de privacidad</a></p>
    <p>Desarrollado por <a href="https://www.instagram.com/sageedev/" target="_blank" rel="noopener">@sageeDev</a></p>
  </div>
</footer>
'''

def tail(msg=WA):
    return f'''
<a class="wa-float js-wa" id="waFloat" href="#" data-msg="{msg}" aria-label="Escribir por WhatsApp"><i class="ti ti-brand-whatsapp"></i></a>

<script src="./main.js"></script>
</body>
</html>
'''

def ph(img, pos, crumb, h1, lead, ctas=True, msg=WA, short=False):
    bg = f'  <div class="ph-bg" aria-hidden="true" style="background-image:url(\'./img/{img}.jpg\');background-position:{pos}"></div>\n' if img else ""
    px = f"<!-- foto de fondo: https://images.pexels.com/photos/{PX[img]}/pexels-photo-{PX[img]}.jpeg -->\n" if img else ""
    c = f'''    <div class="ph-ctas rise d3">
      <a class="btn btn-bordo js-wa" href="#" data-msg="{msg}">Consultar por WhatsApp</a>
      <a class="btn btn-line" href="./index.html#contacto">Completar el formulario</a>
    </div>
''' if ctas else ""
    return f'''
<!-- ============ CABECERA ============ -->
{px}<section class="ph{' ph-short' if short else ''}">
{bg}  <div class="wrap ph-in">
    <nav aria-label="Ruta"><ol class="crumbs"><li><a href="./index.html">Inicio</a></li><li><i class="ti ti-chevron-right" aria-hidden="true"></i><span aria-current="page">{crumb}</span></li></ol></nav>
    <h1 class="ph-h1 split-words">{h1[0]} <em>{h1[1]}</em></h1>
    <p class="lead rise d2">{lead}</p>
{c}  </div>
</section>
'''

def cta(h2, lead, msg=WA):
    return f'''
<!-- ============ CTA ============ -->
<section class="cta-band">
  <div class="cta-bg" aria-hidden="true"></div>
  <div class="wrap reveal">
    <h2 class="h2">{h2[0]} <em>{h2[1]}</em></h2>
    <p class="lead">{lead}</p>
    <div class="cta-ctas">
      <a class="btn btn-bordo js-wa" href="#" data-msg="{msg}">Consultar por WhatsApp</a>
      <a class="btn btn-line" href="./index.html#contacto">Completar el formulario</a>
    </div>
  </div>
</section>
'''

def write(name, html):
    open(name, "w", encoding="utf8", newline="\n").write(html)
    print("ok", name)

SOC = ["Asesoramiento sobre los tipos societarios", "Redacción del contrato social o estatuto",
       "Inscripción en la IGJ o en la Dirección Provincial de Personas Jurídicas", "Redacción y publicación de edictos",
       "Modificaciones del contrato o del estatuto", "Cambios del objeto social", "Aumentos y reducciones de capital",
       "Cualquier otro trámite societario"]

# ================================================================== EL ESTUDIO
estudio = head("El estudio | ACP Estudio Jurídico Contable",
  "Desde 2012 acompañamos a personas, empresas y organizaciones del AMBA. Un estudio versátil y ético que une la mirada contable y la jurídica.") + header("estudio.html") + "\n<main>\n" + ph(
  "columnas", "center 40%", "El estudio", ("Un estudio versátil,", "ético y cercano."),
  "Desde 2012 acompañamos a personas, pequeñas empresas, corporaciones y organizaciones sin fines de lucro del AMBA para que entiendan en detalle su contabilidad, sus impuestos y sus finanzas.") + '''
<!-- ============ ENFOQUE ============ -->
<section class="sobre">
  <div class="wrap">
    <div class="sobre-grid">
      <div class="reveal">
        <p class="eyebrow">Nuestro enfoque</p>
        <h2 class="h2">Cada caso, <em>mirado completo.</em></h2>
      </div>
      <div class="sobre-txt reveal">
        <p>La suma de un contador y un abogado nos permite ver las consecuencias impositivas de una decisión legal y las implicancias legales de una decisión económica.</p>
        <p>Ya sea que necesites un servicio contable, impositivo, de liquidación de sueldos, asesoramiento financiero o legal, buscamos la solución adecuada para tu situación, con el objetivo de que tomes mejores decisiones y cuides tus resultados.</p>
      </div>
    </div>
    <ul class="valores">
      <li class="reveal"><i class="ti ti-arrows-join-2"></i><h3>Integral</h3><p>Lo contable y lo jurídico, coordinados en el mismo estudio y con la misma información.</p></li>
      <li class="reveal"><i class="ti ti-shield-check"></i><h3>Ético</h3><p>Asesoramiento claro y honesto, con la responsabilidad profesional como base.</p></li>
      <li class="reveal"><i class="ti ti-adjustments-horizontal"></i><h3>A medida</h3><p>Soluciones pensadas para tu actividad, tu rubro y tu momento.</p></li>
    </ul>
  </div>
</section>

<!-- ============ PROFESIONALES ============ -->
<section class="profes">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Profesionales</p>
      <h2 class="h2">Quiénes <em>te atienden.</em></h2>
    </div>
    <div class="duo duo-dark">
      <article class="duo-col reveal">
        <p class="duo-tag">Área contable</p>
        <h3>Gabriel Álvarez</h3>
        <p class="duo-role">Contador Público · C.P.C.E.C.A.B.A. T° 390 F° 26</p>
        <p class="duo-txt">A cargo del área contable, impositiva y societaria: impuestos, monotributo, sueldos, certificaciones y constitución de sociedades.</p>
        <a href="./servicios-contables.html" class="link-arrow">Servicios contables <i class="ti ti-arrow-right"></i></a>
      </article>
      <div class="duo-axis" aria-hidden="true">
        <span class="duo-line"></span>
        <span class="duo-iso"><img src="./isotipo-claro.png" alt="" width="174" height="127"></span>
        <span class="duo-line"></span>
      </div>
      <article class="duo-col reveal">
        <p class="duo-tag">Área jurídica</p>
        <h3>Dr. Adrián Calderaro Papa</h3>
        <p class="duo-role">Abogado · C.P.A.C.F. T° 113 F° 31</p>
        <p class="duo-txt">Graduado en la UBA, con siete años en la Justicia Nacional en lo Comercial y experiencia en litigios, concursos y resolución alternativa de conflictos.</p>
        <a href="./servicios-juridicos.html#trayectoria" class="link-arrow">Ver trayectoria <i class="ti ti-arrow-right"></i></a>
      </article>
    </div>
  </div>
</section>

<!-- ============ RUBROS ============ -->
<section class="rubros-sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Industrias</p>
      <h2 class="h2">Rubros que <em>conocemos a fondo.</em></h2>
      <p class="lead">En algunos mercados, un contador general no ofrece exactamente lo que se necesita. Conocemos los detalles de cada uno.</p>
    </div>
    <ul class="valores valores-4">
      <li class="reveal"><i class="ti ti-movie"></i><h3>Entretenimiento</h3><p>Un enfoque personalizado para una industria con reglas propias.</p></li>
      <li class="reveal"><i class="ti ti-building"></i><h3>Inmobiliario</h3><p>Servicios adaptados a desarrollos, alquileres y operaciones.</p></li>
      <li class="reveal"><i class="ti ti-cpu"></i><h3>Tecnología</h3><p>Uno de los sectores que más crecieron en los últimos años.</p></li>
      <li class="reveal"><i class="ti ti-briefcase"></i><h3>Servicios</h3><p>Uno de los rubros que más conocemos y acompañamos.</p></li>
    </ul>
  </div>
</section>
''' + cta(("¿Querés que analicemos", "tu situación?"), "Escribinos por WhatsApp o completá el formulario y te contactamos.") + "\n</main>\n" + FOOTER + tail()
write("estudio.html", estudio)

# ================================================================== SERVICIOS CONTABLES
SVC = [
 ("regimen-general", "Régimen General", "ti-file-invoice", "Asesoramiento a medida para toda clase de actividad comercial, contemplando la situación de cada cliente y los regímenes impositivos vigentes: IVA, Ingresos Brutos (régimen general y Convenio Multilateral), Ganancias, Bienes Personales e Impuestos Internos, entre otros.", "Hola, quisiera consultar por asesoramiento impositivo (Régimen General)."),
 ("monotributo", "Monotributo", "ti-user-dollar", "Asesoramos y acompañamos a los nuevos emprendedores desde la inscripción en el Monotributo, en los regímenes simplificados de Ingresos Brutos y en cada recategorización.", "Hola, quisiera consultar por el Monotributo."),
 ("empresas", "Empresas y PyMEs", "ti-building-store", "Precisión, puntualidad y atención al detalle. Hoy los negocios necesitan un análisis cuidadoso de sus aspectos contables e impositivos para ser competitivos, y ese es el foco de este servicio.", "Hola, quisiera consultar por asesoramiento contable para mi empresa."),
 ("sueldos", "Sueldos y RR. HH.", "ti-users", "Liquidación de haberes del personal, aportes y contribuciones al Sistema Único de la Seguridad Social, cuotas sindicales, y altas y bajas de empleados.", "Hola, quisiera consultar por liquidación de sueldos."),
 ("retenciones", "Agentes de retención y percepción", "ti-receipt-tax", "Si sos agente de retención o percepción de impuestos, te asesoramos y liquidamos a medida los distintos regímenes vigentes.", "Hola, soy agente de retención y percepción y quisiera hacer una consulta."),
]
OTROS = ["Auditorías", "Certificaciones de ingresos", "Certificaciones contables", "Declaraciones juradas ante la Oficina Anticorrupción",
         "Manifestaciones de bienes", "Moratorias y planes de facilidades de pago", "Requerimientos bancarios", "Asesoramiento de costos", "Trámites ante ARCA"]
svc_html = "\n".join(f'''      <article class="svc-row reveal" id="{sid}">
        <div class="svc-row-head"><span class="svc-n">0{i+1}</span><i class="ti {ic}"></i><h3>{t}</h3></div>
        <div class="svc-row-body"><p>{d}</p><a class="link-arrow js-wa" href="#" data-msg="{m}">Consultar por este servicio <i class="ti ti-arrow-right"></i></a></div>
      </article>''' for i, (sid, t, ic, d, m) in enumerate(SVC))
otros_html = "\n".join(f'      <li class="reveal"><i class="ti ti-check"></i>{o}</li>' for o in OTROS)
soc_html = "\n".join(f'      <li><i class="ti ti-check"></i>{s}</li>' for s in SOC)
cont = head("Servicios contables | Impuestos, monotributo, sueldos y sociedades | ACP",
  "Asesoramiento contable e impositivo en CABA: Régimen General, Monotributo, empresas y PyMEs, liquidación de sueldos, agentes de retención, certificaciones y sociedades comerciales.") + header("servicios-contables.html") + "\n<main>\n" + ph(
  "fachada", "center 50%", "Servicios contables", ("Servicios contables", "para personas y empresas."),
  "Soluciones a medida de cada actividad, con los regímenes impositivos vigentes y la puntualidad que exige el día a día de un negocio.") + f'''
<!-- ============ SERVICIOS ============ -->
<section class="svc-sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Qué hacemos</p>
      <h2 class="h2">Impuestos, sueldos <em>y gestión contable.</em></h2>
    </div>
    <div class="svc-rows">
{svc_html}
    </div>
  </div>
</section>

<!-- ============ OTROS SERVICIOS ============ -->
<section class="otros" id="tramites">
  <div class="wrap otros-grid">
    <div class="reveal">
      <p class="eyebrow">Certificaciones y trámites</p>
      <h2 class="h2">Otros servicios <em>del área.</em></h2>
      <p class="lead">También te asesoramos en trámites y en la información que tenés que presentar ante distintas entidades. Consultanos por cualquier otro.</p>
    </div>
    <ul class="otros-list">
{otros_html}
    </ul>
  </div>
</section>

<!-- ============ SOCIEDADES ============ -->
<section class="sociedades" id="sociedades">
  <div class="soc-bg" aria-hidden="true"></div>
  <div class="wrap soc-grid">
    <div class="reveal">
      <p class="eyebrow eb-light">Sociedades comerciales</p>
      <h2 class="h2">Creá tu sociedad <em>con nosotros.</em></h2>
      <p class="lead">Te ayudamos a elegir el tipo societario que mejor se adapte a tu proyecto y nos ocupamos del trámite completo, con la parte contable y la legal en el mismo estudio.</p>
      <a class="btn btn-paper js-wa" href="#" data-msg="Hola, quisiera constituir una sociedad.">Consultar por una sociedad</a>
    </div>
    <ul class="soc-list reveal">
{soc_html}
    </ul>
  </div>
</section>
''' + cta(("Estamos para ayudarte,", "contanos qué necesitás."), "Te respondemos a la brevedad por WhatsApp o por email.") + "\n</main>\n" + FOOTER + tail()
write("servicios-contables.html", cont)

# ================================================================== SERVICIOS JURÍDICOS
AREAS = [
 ("ti-scale", "Litigios civiles y comerciales", "Representación de personas y empresas en juicios civiles y comerciales, con el conocimiento del fuero comercial desde adentro."),
 ("ti-briefcase", "Derecho laboral", "Intervención en litigios laborales, individuales y colectivos."),
 ("ti-building-bank", "Concursos y quiebras", "Concursos preventivos, quiebras y procesos universales, una especialidad que también enseñó en la UBA."),
 ("ti-users-group", "Acciones colectivas", "Defensa de entidades financieras y compañías de seguros en acciones colectivas."),
 ("ti-receipt-tax", "Reclamos administrativos y tributarios", "Reclamos contenciosos, administrativos y tributarios, coordinados con el área contable."),
 ("ti-arrows-exchange", "Mediación, negociación y arbitraje", "Resolución alternativa de conflictos para evitar un juicio o acortarlo."),
 ("ti-file-search", "Auditoría de litigios", "Relevamiento, compulsa y auditoría de carteras de juicios individuales y universales."),
 ("ti-building-skyscraper", "Asesoramiento corporativo", "Acompañamiento legal a empresas en sus decisiones y conflictos del día a día."),
]
TL = [
 ("2008", "Abogado por la Universidad de Buenos Aires", "Se gradúa en la UBA y continúa su formación con los tres Cursos Anuales para empleados judiciales de la Cámara Nacional de Apelaciones en lo Comercial y con programas de actualización en Derecho Civil y Comercial de la Facultad de Derecho."),
 ("7 años", "Justicia Nacional en lo Comercial", "Ocupa distintos cargos en el Fuero Comercial del Poder Judicial de la Nación: despacho integral de litigios, conciliación de audiencias y proyectos de resoluciones y sentencias en procesos universales y contradictorios."),
 ("Estudio BSCP", "Abogado senior", "Se desempeña como abogado senior del Estudio Jurídico BSCP, liderado por los Dres. Santiago Bargalló Beade y Marcelo Eugenio Griffi."),
 ("UBA", "Docencia e investigación", "Fue docente de Concursos y Quiebras en la Facultad de Derecho de la UBA, disertante del taller «¿Cómo analizar un fallo?» y expositor de la charla «Metodología de estudio». Participó en más de dos docenas de jornadas, seminarios y conferencias."),
 ("ACP", "Estudio propio", "Funda su estudio y luego se une al contador Gabriel Álvarez para ofrecer, desde ACP, asesoramiento jurídico y contable integrado."),
]
areas_html = "\n".join(f'      <li class="reveal"><i class="ti {ic}"></i><h3>{t}</h3><p>{d}</p></li>' for ic, t, d in AREAS)
tl_html = "\n".join(f'      <li class="reveal"><span class="tl-k">{k}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for k, t, d in TL)
jur = head("Servicios jurídicos | Litigios, concursos y mediación en CABA | ACP",
  "Abogado en CABA con siete años en la Justicia Nacional en lo Comercial: litigios civiles, comerciales y laborales, concursos y quiebras, mediación, arbitraje y asesoramiento a empresas.") + header("servicios-juridicos.html") + "\n<main>\n" + ph(
  "libros", "center 50%", "Servicios jurídicos", ("Servicios jurídicos", "con experiencia en tribunales."),
  "Asesoramos y representamos a personas y empresas en litigios, reclamos y procesos de resolución alternativa de conflictos.",
  msg="Hola, quisiera hacer una consulta legal.") + f'''
<!-- ============ ÁREAS ============ -->
<section class="juridico">
  <div class="wrap">
    <div class="sec-head reveal">
      <p class="eyebrow">Áreas de experiencia</p>
      <h2 class="h2">Procesal, civil, <em>comercial y laboral.</em></h2>
      <p class="lead">Individual, colectivo y corporativo: desde el litigio hasta la negociación, la mediación y el arbitraje.</p>
    </div>
    <ul class="areas areas-4">
{areas_html}
    </ul>
  </div>
</section>

<!-- ============ TRAYECTORIA ============ -->
<section class="trayectoria" id="trayectoria">
  <div class="wrap">
    <div class="tray-grid">
      <div class="tray-head reveal">
        <p class="eyebrow">Trayectoria</p>
        <h2 class="h2">Dr. Adrián <em>Calderaro Papa.</em></h2>
        <p class="lead">Abogado · C.P.A.C.F. T° 113 F° 31</p>
        <ul class="cifras cifras-dark" aria-label="Trayectoria en cifras">
          <li><b><span class="count" data-to="18" data-prefix="+">+18</span></b><small>años de trayectoria</small></li>
          <li><b><span class="count" data-to="7">7</span></b><small>años en la Justicia Nacional en lo Comercial</small></li>
        </ul>
        <a href="mailto:acalderaro@acpestudio.com.ar" class="link-arrow">acalderaro@acpestudio.com.ar <i class="ti ti-arrow-right"></i></a>
      </div>
      <ol class="tl">
{tl_html}
      </ol>
    </div>
  </div>
</section>
''' + cta(("¿Tenés un conflicto legal", "o un juicio en curso?"), "Contanos tu situación y te decimos cómo podemos ayudarte.", "Hola, quisiera hacer una consulta legal.") + "\n</main>\n" + FOOTER + tail("Hola, quisiera hacer una consulta legal.")
write("servicios-juridicos.html", jur)

# ================================================================== PRIVACIDAD
priv = head("Política de privacidad | ACP Estudio Jurídico Contable", "Cómo trata ACP los datos personales que recibe a través de este sitio, conforme a la Ley 25.326.") + header() + "\n<main>\n" + ph(
  None, "", "Política de privacidad", ("Política", "de privacidad."), "Cómo tratamos los datos que nos enviás a través de este sitio.", ctas=False, short=True) + '''
<section class="legal">
  <div class="wrap legal-in">
    <p class="legal-date">Última actualización: octubre de 2026</p>
    <h2>1. Responsables</h2>
    <p>Los responsables del tratamiento son Gabriel Álvarez (Contador Público, C.P.C.E.C.A.B.A. T° 390 F° 26) y Adrián Calderaro Papa (Abogado, C.P.A.C.F. T° 113 F° 31), con domicilio en Av. Entre Ríos 1243, Ciudad Autónoma de Buenos Aires. Podés contactarnos por WhatsApp al 11 5760-7128 o por email a acalderaro@acpestudio.com.ar.</p>
    <h2>2. Qué datos recopilamos</h2>
    <p>Solo los que nos enviás voluntariamente: tu nombre, email, teléfono (opcional), el tema de tu consulta y el mensaje que escribís en el formulario, o los datos que compartís al escribirnos por WhatsApp. El sitio no usa cookies de seguimiento ni herramientas de publicidad.</p>
    <h2>3. Para qué los usamos</h2>
    <p>Para responder tu consulta, coordinar una reunión y, si decidís contratarnos, prestar el servicio. No usamos tus datos para otros fines ni los cedemos a terceros con fines comerciales.</p>
    <h2>4. Secreto profesional</h2>
    <p>La información que nos confiás está protegida por el secreto profesional que rige el ejercicio de la abogacía y de las ciencias económicas.</p>
    <h2>5. Servicios de terceros</h2>
    <p>Para funcionar, el sitio usa servicios externos que pueden procesar datos técnicos (como la dirección IP):</p>
    <ul>
      <li><b>FormSubmit</b>, que envía a nuestro correo los datos del formulario de contacto.</li>
      <li><b>WhatsApp</b> (Meta Platforms), si elegís escribirnos por ese medio.</li>
      <li><b>Google Fonts</b> y <b>jsDelivr</b>, que sirven las tipografías y los íconos del sitio.</li>
    </ul>
    <p>Cada uno se rige por su propia política de privacidad.</p>
    <h2>6. Conservación y seguridad</h2>
    <p>Conservamos los datos el tiempo necesario para atender tu consulta y cumplir obligaciones legales y profesionales, y aplicamos medidas razonables para protegerlos.</p>
    <h2>7. Tus derechos</h2>
    <p>Conforme a la Ley 25.326, podés solicitar en forma gratuita el acceso, la rectificación, la actualización o la supresión de tus datos, contactándonos por los medios indicados en el punto 1. La Agencia de Acceso a la Información Pública, órgano de control de la Ley 25.326, atiende las denuncias y los reclamos por incumplimientos de las normas sobre protección de datos personales.</p>
    <h2>8. Cambios</h2>
    <p>Podemos actualizar esta política. La versión vigente es siempre la publicada en esta página.</p>
  </div>
</section>
''' + "\n</main>\n" + FOOTER + tail()
write("privacidad.html", priv)

# ================================================================== 404
nf = head("Página no encontrada | ACP Estudio Jurídico Contable", "La página que buscás no existe o cambió de dirección.", robots="noindex") + header() + f'''
<main>
<section class="nf">
  <div class="nf-bg" aria-hidden="true"></div>
  <div class="wrap nf-in">
    <span class="nf-num" aria-hidden="true">404</span>
    <h1 class="ph-h1">Esta página <em>no existe.</em></h1>
    <p class="lead">Puede que haya cambiado de dirección. Volvé al inicio o escribinos y te ayudamos.</p>
    <div class="ph-ctas">
      <a class="btn btn-bordo" href="./index.html">Volver al inicio</a>
      <a class="btn btn-line js-wa" href="#" data-msg="{WA}">Consultar por WhatsApp</a>
    </div>
  </div>
</section>
</main>
''' + FOOTER + tail()
write("404.html", nf)
