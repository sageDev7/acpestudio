"""Agrega al styles.css los componentes de las páginas internas (idempotente)."""
import os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(D)
c = open("styles.css", encoding="utf8").read()
MARK = "/* =========================================================\n   PÁGINAS INTERNAS"
if MARK in c:
    a = c.index(MARK); b = c.index("/* =========================================================\n   RESPONSIVE")
    c = c[:a] + c[b:]
    c = c[:c.index("\n/* ---------- páginas internas: responsive ---------- */")] if "páginas internas: responsive" in c else c

BASE = r'''/* =========================================================
   PÁGINAS INTERNAS
   ========================================================= */
.nav a[aria-current]::after{transform:scaleX(1)}
.mnav a[aria-current]{color:var(--sand)}

/* ---------- cabecera de página ---------- */
.ph{position:relative;min-height:74vh;min-height:74svh;display:flex;align-items:flex-end;overflow:hidden;background:var(--ink);isolation:isolate;padding:calc(var(--hdr) + 4rem) 0 5.5rem}
.ph-short{min-height:0;padding:calc(var(--hdr) + 5rem) 0 4.5rem;background:linear-gradient(120deg,var(--ink) 0%,var(--night-2) 65%,var(--bordo-x) 100%)}
.ph-bg{position:absolute;inset:-8% 0 0;z-index:-2;background-size:cover;background-repeat:no-repeat;filter:grayscale(.6) brightness(.72);will-change:transform}
.ph:not(.ph-short)::after{content:"";position:absolute;inset:0;z-index:-1;background:
  linear-gradient(95deg,rgba(14,12,11,.96) 0%,rgba(14,12,11,.86) 45%,rgba(14,12,11,.45) 80%,rgba(58,18,16,.45) 100%),
  linear-gradient(0deg,rgba(14,12,11,.9) 0%,transparent 55%)}
.ph-in{position:relative;z-index:1;width:100%}
.crumbs{display:flex;flex-wrap:wrap;align-items:center;gap:.5rem;margin-bottom:1.6rem;font-size:.7rem;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:var(--muted-l)}
.crumbs li{display:flex;align-items:center;gap:.5rem}
.crumbs a{transition:color .3s}
.crumbs a:hover{color:var(--sand)}
.crumbs i{font-size:.8rem;color:var(--bordo)}
.crumbs [aria-current]{color:var(--sand)}
.ph-h1{font-size:clamp(2.5rem,5vw,4.4rem);line-height:1.06;max-width:min(100%,16em)}
.ph-h1 em{display:block;font-style:normal;color:var(--sand)}
.ph .lead{margin-top:1.4rem;max-width:40rem}
.ph-ctas{display:flex;flex-wrap:wrap;gap:1rem;margin-top:2.2rem}

/* ---------- secciones claras compartidas ---------- */
.sobre,.svc-sec,.cta-band,.legal{background:var(--paper);color:var(--text)}
.sobre .h2,.svc-sec .h2,.cta-band .h2,.sobre h3,.svc-sec h3,.legal h2{color:var(--ink)}
.sobre .h2 em,.svc-sec .h2 em,.cta-band .h2 em{color:var(--bordo)}
.sobre .eyebrow,.svc-sec .eyebrow,.cta-band .eyebrow{color:var(--bordo)}
.sobre .lead,.svc-sec .lead,.cta-band .lead{color:var(--muted)}

/* ---------- el estudio ---------- */
.sobre{padding:140px 0}
.sobre-grid{display:grid;grid-template-columns:.85fr 1.15fr;gap:5rem;align-items:start;margin-bottom:4.5rem}
.sobre-txt p{margin-bottom:1.2rem;color:var(--muted)}
.sobre-txt p:first-child{font-family:var(--head);font-size:clamp(1.3rem,2vw,1.6rem);line-height:1.45;color:var(--ink)}
.valores{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2rem}
.valores-4{grid-template-columns:repeat(4,1fr)}
.valores li{position:relative;padding:2.3rem 2rem;background:#FBF8F3;border:1px solid var(--line);transition:transform .5s var(--ease),box-shadow .5s,border-color .5s}
.valores li::after{content:"";position:absolute;left:0;bottom:0;width:100%;height:2px;background:var(--bordo);transform:scaleX(0);transform-origin:left;transition:transform .6s var(--ease)}
.valores li:hover{transform:translateY(-4px);box-shadow:0 18px 40px -24px rgba(42,36,33,.35);border-color:transparent}
.valores li:hover::after{transform:scaleX(1)}
.valores i{display:block;margin-bottom:1.2rem;font-size:1.9rem;color:var(--bordo)}
.valores h3{margin-bottom:.5rem;font-size:1.45rem;color:var(--ink)}
.valores p{font-size:.96rem;color:var(--muted)}
.valores li.reveal:nth-child(2){transition-delay:.08s}.valores li.reveal:nth-child(3){transition-delay:.16s}.valores li.reveal:nth-child(4){transition-delay:.24s}
.profes{padding:140px 0;background:var(--night)}
.duo-dark .duo-tag{color:var(--sand)}
.duo-dark h3{color:var(--paper)}
.duo-dark .duo-role{color:var(--muted-l)}
.duo-txt{max-width:26rem;margin-bottom:1.8rem;color:var(--muted-l)}
.duo-dark .duo-col:first-child .duo-txt{margin-left:auto}
.duo-dark .duo-iso{background:var(--bordo-x);box-shadow:0 0 0 8px var(--night),0 0 0 9px rgba(203,181,157,.35)}
.duo-dark .link-arrow{color:var(--paper)}
.duo-dark .link-arrow:hover{color:var(--sand)}
.rubros-sec{padding:130px 0;background:var(--bordo-x)}
.rubros-sec .eyebrow{color:var(--paper)}
.rubros-sec .eyebrow::before,.rubros-sec .sec-head .eyebrow::after{background:var(--paper)}
.rubros-sec .h2 em{color:var(--paper);opacity:.75}
.rubros-sec .lead{color:rgba(243,237,227,.78)}
.rubros-sec .valores li{background:rgba(243,237,227,.05);border-color:rgba(243,237,227,.12)}
.rubros-sec .valores li::after{background:var(--sand)}
.rubros-sec .valores li:hover{box-shadow:none;background:rgba(243,237,227,.09)}
.rubros-sec .valores i{color:var(--sand)}
.rubros-sec .valores h3{color:var(--paper)}
.rubros-sec .valores p{color:rgba(243,237,227,.72)}

/* ---------- servicios contables ---------- */
.svc-sec{padding:140px 0}
.svc-rows{border-top:1px solid var(--line)}
.svc-row{display:grid;grid-template-columns:.9fr 1.1fr;gap:4rem;padding:2.6rem .4rem;border-bottom:1px solid var(--line);scroll-margin-top:calc(var(--hdr) + 1rem)}
.svc-row-head{display:flex;align-items:center;gap:1.1rem}
.svc-row-head .svc-n{color:var(--bordo)}
.svc-row-head i{font-size:1.6rem;color:var(--bordo)}
.svc-row h3{font-size:clamp(1.5rem,2.3vw,1.95rem)}
.svc-row-body p{margin-bottom:1.3rem;color:var(--muted)}
.svc-row-body .link-arrow{color:var(--ink)}
.svc-row-body .link-arrow:hover{color:var(--bordo)}
.otros{padding:130px 0;background:var(--night);scroll-margin-top:var(--hdr)}
.otros-grid{display:grid;grid-template-columns:.85fr 1.15fr;gap:5rem;align-items:start}
.otros .lead{margin-top:1.3rem}
.otros-list{display:grid;grid-template-columns:1fr 1fr;gap:.9rem 1.2rem}
.otros-list li{display:flex;align-items:flex-start;gap:.8rem;padding:1.05rem 1.2rem;background:rgba(243,237,227,.04);border-left:2px solid var(--bordo);font-size:.98rem}
.otros-list i{flex:none;margin-top:.25rem;color:var(--sand)}
.sociedades{scroll-margin-top:var(--hdr)}

/* ---------- servicios jurídicos ---------- */
.areas-4{grid-template-columns:repeat(4,1fr)}
.trayectoria{padding:140px 0;background:var(--night);scroll-margin-top:var(--hdr)}
.tray-grid{display:grid;grid-template-columns:.8fr 1.2fr;gap:5rem;align-items:start}
.tray-head{position:sticky;top:calc(var(--hdr) + 2rem)}
.tray-head .lead{margin:.9rem 0 2rem}
.cifras-dark{margin-bottom:2.2rem;border-color:var(--line-l)}
.cifras-dark li{border-color:var(--line-l)}
.cifras-dark b{color:var(--sand)}
.cifras-dark small{color:var(--muted-l)}
.trayectoria .link-arrow{color:var(--paper);text-transform:none;letter-spacing:.02em;font-size:.95rem;overflow-wrap:anywhere}
.tl{position:relative}
.tl::before{content:"";position:absolute;left:5.6rem;top:.6rem;bottom:.6rem;width:1px;background:linear-gradient(var(--bordo),rgba(147,49,44,.15))}
.tl li{position:relative;display:grid;grid-template-columns:5.6rem 1fr;gap:2.4rem;padding-bottom:2.6rem}
.tl li:last-child{padding-bottom:0}
.tl li::after{content:"";position:absolute;left:5.6rem;top:.55rem;width:11px;height:11px;margin-left:-5px;border-radius:50%;background:var(--night);border:1px solid var(--sand);transition:background .6s .3s}
.tl li.in::after{background:var(--bordo);border-color:var(--bordo)}
.tl-k{font-family:var(--head);font-size:1.15rem;line-height:1.35;color:var(--sand);text-align:right}
.tl h3{margin-bottom:.45rem;font-size:1.4rem}
.tl p{font-size:.97rem;color:var(--muted-l)}

/* ---------- cierre (claro: no se mezcla con el footer) ---------- */
.cta-band{position:relative;padding:130px 0;overflow:hidden;text-align:center;isolation:isolate}
.cta-bg{position:absolute;left:50%;top:50%;z-index:-1;width:min(520px,80vw);aspect-ratio:174/127;transform:translate(-50%,-50%);background:url('./isotipo.png') center/contain no-repeat;opacity:.05}
.cta-band .h2{max-width:46rem;margin:0 auto}
.cta-band .lead{max-width:36rem;margin:1.2rem auto 0}
.cta-ctas{display:flex;justify-content:center;flex-wrap:wrap;gap:1rem;margin-top:2.3rem}
.cta-band .btn-line{border-color:rgba(42,36,33,.4);color:var(--ink)}
.cta-band .btn-line::before{background:var(--ink)}
.cta-band .btn-line:hover{color:var(--paper);border-color:var(--ink)}

/* ---------- privacidad ---------- */
.legal{padding:100px 0 130px}
.legal-in{max-width:46rem}
.legal-date{margin-bottom:2.4rem;font-size:.85rem;font-weight:600;color:var(--bordo)}
.legal h2{margin:2.6rem 0 .8rem;font-size:1.5rem}
.legal p,.legal li{color:var(--muted)}
.legal p+p{margin-top:.8rem}
.legal ul{display:grid;gap:.5rem;margin:.8rem 0}
.legal li{position:relative;padding-left:1.3rem}
.legal li::before{content:"";position:absolute;left:0;top:.8em;width:.55rem;height:1px;background:var(--bordo)}
.legal b{color:var(--ink)}

/* ---------- 404 ---------- */
.nf{position:relative;min-height:100vh;min-height:100svh;display:flex;align-items:center;overflow:hidden;background:var(--ink);isolation:isolate;padding:calc(var(--hdr) + 3rem) 0 4rem}
.nf-bg{position:absolute;inset:0;z-index:-2;background:url('./img/hero-noche.jpg') center/cover no-repeat;filter:grayscale(.6) brightness(.55)}
.nf::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(95deg,rgba(14,12,11,.97) 0%,rgba(14,12,11,.85) 55%,rgba(58,18,16,.55) 100%)}
.nf-num{display:block;margin-bottom:1rem;font-family:var(--head);font-size:clamp(6rem,14vw,11rem);line-height:.85;color:var(--bordo)}
.nf .lead{margin-top:1.3rem;max-width:34rem}

'''
RESP = r'''
/* ---------- páginas internas: responsive ---------- */
@media (max-width:1024px){
  .sobre-grid,.otros-grid,.tray-grid{grid-template-columns:1fr;gap:2.6rem}
  .valores,.valores-4,.areas-4{grid-template-columns:1fr 1fr}
  .valores li.reveal:nth-child(n){transition-delay:0s}
  .svc-row{grid-template-columns:1fr;gap:1.2rem}
  .tray-head{position:static}
}
@media (max-width:768px){
  .ph{min-height:0;padding:calc(var(--hdr) + 3.5rem) 0 4rem;text-align:center}
  .ph-short{padding:calc(var(--hdr) + 3rem) 0 3.2rem}
  .ph:not(.ph-short)::after{background:linear-gradient(180deg,rgba(14,12,11,.8) 0%,rgba(14,12,11,.86) 55%,rgba(14,12,11,.97) 100%)}
  .crumbs{justify-content:center;font-size:.62rem;letter-spacing:.14em}
  .ph-h1{font-size:clamp(2.1rem,9vw,2.8rem);max-width:none}
  .ph .lead{margin-left:auto;margin-right:auto;font-size:1rem}
  .ph-ctas{flex-direction:column;align-items:center}
  .ph-ctas .btn{width:100%;max-width:300px}
  .sobre,.profes,.rubros-sec,.svc-sec,.otros,.trayectoria,.cta-band,.legal{padding:84px 0}
  .sobre-grid{margin-bottom:3rem}
  .sobre-grid>div:first-child,.sobre-txt,.otros-grid>div:first-child,.tray-head{text-align:center}
  .valores,.valores-4,.areas-4{grid-template-columns:1fr}
  .valores li{padding:2rem 1.5rem;text-align:center}
  .duo-txt,.duo-dark .duo-col:first-child .duo-txt{margin-left:auto;margin-right:auto}
  .svc-row{padding:2.2rem .2rem;text-align:center}
  .svc-row-head{flex-direction:column;gap:.5rem}
  .otros-list{grid-template-columns:1fr;max-width:26rem;margin:0 auto}
  .cifras-dark{max-width:24rem;margin-left:auto;margin-right:auto}
  .tl::before{left:.4rem}
  .tl li{grid-template-columns:1fr;gap:.3rem;padding-left:2.2rem}
  .tl li::after{left:.4rem}
  .tl-k{text-align:left}
  .cta-ctas{flex-direction:column;align-items:center}
  .cta-ctas .btn{width:100%;max-width:300px}
  .nf{text-align:center}
  .nf .lead{margin-left:auto;margin-right:auto}
}
'''
i = c.index("/* =========================================================\n   RESPONSIVE")
c = c[:i] + BASE + c[i:] + RESP
open("styles.css", "w", encoding="utf8").write(c)
print("ok")
