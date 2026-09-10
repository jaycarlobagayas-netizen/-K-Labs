import json
pubs=json.load(open('pubs.json'))
pubs.sort(key=lambda p:(-p['y'], not p['scopus'], p['t']))
years=sorted({p['y'] for p in pubs})
by={y:sum(1 for p in pubs if p['y']==y) for y in years}
sc=sum(1 for p in pubs if p['scopus']); ns=len(pubs)-sc

scholars=[
 ("Jay Carlo S. Bagayas, MSPE","Faculty · Bachelor of Physical Education","csQoCo4AAAAJ","JB"),
 ("Jessel Gay Wacan, MSPE","Chairperson · Bachelor of Physical Education","khPU-9kAAAAJ","JW"),
 ("Steffany Anne C. Poblador, LPT","Faculty · Bachelor of Physical Education","49Vw-4sAAAAJ","SP"),
 ("Lorie Martin, MSc","Faculty · Bachelor of Physical Education","YiXWO2IAAAAJ","LM"),
 ("Sammielyn Lavente, MAEd-PE","Faculty · Bachelor of Physical Education","BZdY-XMAAAAJ","SL"),
]

cards=[]
for i,p in enumerate(pubs):
    d=' d1' if i%2 else ''
    tags=f'<span class="pub-year">{p["y"]}</span><span class="pub-type">{p["type"]}</span>'
    if not p['scopus']: tags+='<span class="pub-nonscopus">Non-Scopus</span>'
    doi=(f'<a class="pub-doi" href="https://doi.org/{p["doi"]}" target="_blank" rel="noopener">DOI: {p["doi"]} ↗</a>'
         if p['doi'] else '<span class="pub-doi" style="cursor:default">Published Article</span>')
    cards.append(
      f'      <article class="pub-card reveal{d}" data-year="{p["y"]}" data-scopus="{str(p["scopus"]).lower()}">'
      f'<div class="pub-top">{tags}</div>'
      f'<h3>{p["t"]}</h3>'
      f'<p class="pub-meta">{p["a"]}</p>'
      f'<p class="pub-abs">{p["v"]}</p>{doi}</article>')

sch=[]
for name,role,uid,ini in scholars:
    sch.append(
      f'      <a class="gs-card reveal" href="https://scholar.google.com/citations?user={uid}" target="_blank" rel="noopener">'
      f'<span class="gs-ava" aria-hidden="true">{ini}</span>'
      f'<span class="gs-body"><span class="gs-name">{name}</span><span class="gs-role">{role}</span></span>'
      f'<span class="gs-go" aria-hidden="true">↗</span></a>')

bars="".join(f'{{y:{y},n:{by[y]}}},' for y in years)

html=f'''<!-- PUBLICATIONS -->
<section class="section" id="publications" aria-labelledby="h-pubs">
  <div class="wrap">
    <div class="section-head center reveal">
      <span class="pill">✦ Research Repository</span>
      <h2 id="h-pubs">Research <span class="gold">analytics &amp; publications</span></h2>
      <p>The official repository of scientific publications by the BPED Department faculty.</p>
    </div>

    <!-- ===== RESEARCH ANALYTICS ===== -->
    <div class="ra-kpis reveal">
      <div class="ra-kpi"><span class="ra-num" data-count="{len(pubs)}">0</span><span class="ra-lbl">Total publications</span></div>
      <div class="ra-kpi"><span class="ra-num" data-count="{sc}">0</span><span class="ra-lbl">Scopus-indexed</span></div>
      <div class="ra-kpi"><span class="ra-num" data-count="{len(years)}">0</span><span class="ra-lbl">Years represented</span></div>
      <div class="ra-kpi"><span class="ra-num" data-count="{len(scholars)}">0</span><span class="ra-lbl">Scholar profiles</span></div>
    </div>

    <div class="ra-charts">
      <div class="card reveal">
        <h3>◷ Indexing distribution</h3>
        <div class="ra-donut-wrap">
          <svg id="raDonut" viewBox="0 0 220 220" role="img" aria-label="Pie chart: {sc} Scopus-indexed and {ns} non-Scopus publications"></svg>
          <div class="ra-legend">
            <div class="ra-lg"><span class="ra-dot sc"></span><b>Scopus-indexed</b><i>{sc} papers · {round(sc/len(pubs)*100)}%</i></div>
            <div class="ra-lg"><span class="ra-dot ns"></span><b>Non-Scopus</b><i>{ns} papers · {round(ns/len(pubs)*100)}%</i></div>
          </div>
        </div>
      </div>
      <div class="card reveal">
        <h3>◫ Publications per year</h3>
        <svg id="raBars" viewBox="0 0 560 300" role="img" aria-label="Bar and line chart of publication frequency per year"></svg>
        <p class="ra-cap">Annual output across {years[0]}–{years[-1]}, with a trend line. Bars show total publications; the gold line traces the yearly trajectory.</p>
      </div>
    </div>

    <!-- ===== GOOGLE SCHOLAR ===== -->
    <div class="card reveal" style="margin-top:1.4rem">
      <h3>🎓 Faculty Google Scholar profiles</h3>
      <p class="ra-sub">Live citation records maintained by the faculty. Click any card to open the full profile on Google Scholar.</p>
      <div class="gs-grid">
{chr(10).join(sch)}
      </div>
    </div>

    <div class="feature reveal" style="margin:48px 0">
      <div class="feat-media">
        <span class="badge">Editorial Board · Scopus Q3</span>
        <div class="ph"><div><span class="big">🔬</span><strong>Research Excellence</strong><small>images/research-editorial.jpg</small></div></div>
        <img src="images/research-editorial.jpg" alt="BPED faculty appointed editorial board member of the Journal of Coaching and Sports Science (Scopus Q3)" loading="lazy" onerror="this.style.display='none'">
      </div>
      <div class="feat-body">
        <span class="eyebrow">A research-active department</span>
        <h2 style="margin-top:8px">Strong in <span class="gold">research publication</span></h2>
        <p>BPED faculty publish consistently in <strong>Scopus-indexed, peer-reviewed journals</strong> across sports science, pedagogy, and PE innovation — and even serve on <strong>international editorial boards</strong>, such as the Journal of Coaching and Sports Science (JCSS).</p>
        <p>The department's work extends into <strong>international research collaborations</strong>, including partners such as Universitas Negeri Malang and the University of Portsmouth, United Kingdom.</p>
        <div class="chips">
          <span class="chip gold">Scopus-indexed</span>
          <span class="chip">Sports science</span>
          <span class="chip">PE innovation</span>
          <span class="chip">Global collaborations</span>
        </div>
      </div>
    </div>

    <div class="scopus-banner reveal">
      <span class="scopus-logo" aria-label="Scopus">Scopus<sup>®</sup></span>
      <p>Publications below are indexed in <strong>Scopus</strong>, the world's largest abstract and citation database of peer-reviewed literature, unless tagged <em>Non-Scopus</em>.</p>
    </div>

    <div class="ra-filters reveal" role="group" aria-label="Filter publications">
      <button class="ra-filter is-on" data-filter="all">All ({len(pubs)})</button>
      <button class="ra-filter" data-filter="scopus">Scopus ({sc})</button>
      <button class="ra-filter" data-filter="non">Non-Scopus ({ns})</button>
    </div>

    <div class="bento" style="margin-top:1.4rem;grid-template-columns:repeat(2,1fr)" id="pubList">
{chr(10).join(cards)}
    </div>
  </div>
</section>
'''

css='''
/* ===== RESEARCH ANALYTICS ===== */
.ra-kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:22px}
.ra-kpi{background:linear-gradient(160deg,var(--panel-2),var(--panel));border:1px solid var(--line);border-radius:var(--radius);padding:1.3rem 1.2rem;text-align:center;position:relative;overflow:hidden;transition:border-color .3s,transform .3s}
.ra-kpi::before{content:"";position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--maroon-bright),var(--gold))}
.ra-kpi:hover{border-color:var(--line-gold);transform:translateY(-3px)}
.ra-num{display:block;font-family:var(--grok);font-size:2.1rem;font-weight:700;color:var(--gold);line-height:1}
.ra-lbl{display:block;font-size:.7rem;text-transform:uppercase;letter-spacing:.12em;color:var(--muted);margin-top:.5rem;font-weight:700}
.ra-charts{display:grid;grid-template-columns:.85fr 1.15fr;gap:20px}
.ra-donut-wrap{display:flex;align-items:center;gap:1.2rem;flex-wrap:wrap;justify-content:center}
#raDonut{width:190px;height:190px;flex:none}
.ra-legend{display:flex;flex-direction:column;gap:.9rem;min-width:150px}
.ra-lg{display:grid;grid-template-columns:auto 1fr;gap:.2rem .6rem;align-items:center}
.ra-lg b{color:#fff;font-size:.9rem;font-weight:600}
.ra-lg i{grid-column:2;font-style:normal;font-size:.78rem;color:var(--muted)}
.ra-dot{width:13px;height:13px;border-radius:4px;grid-row:span 2}
.ra-dot.sc{background:linear-gradient(135deg,#f59a4e,#e9711c)}
.ra-dot.ns{background:linear-gradient(135deg,#6b1320,#a52338)}
#raBars{width:100%;height:auto;display:block}
.ra-cap{font-size:.78rem;color:var(--muted);margin-top:.7rem;line-height:1.6}
.ra-sub{font-size:.9rem;color:var(--muted);margin:-.6rem 0 1.1rem}
.gs-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:.8rem}
.gs-card{display:flex;align-items:center;gap:.85rem;background:rgba(255,255,255,.03);border:1px solid var(--line);border-radius:14px;padding:.85rem 1rem;text-decoration:none;transition:border-color .3s,transform .3s,background .3s}
.gs-card:hover{border-color:var(--line-gold);transform:translateY(-3px);background:rgba(242,183,5,.05)}
.gs-ava{width:40px;height:40px;flex:none;border-radius:50%;background:linear-gradient(135deg,var(--maroon),var(--maroon-deep));color:var(--gold);display:grid;place-items:center;font-weight:900;font-size:.82rem;border:2px solid var(--gold)}
.gs-body{display:flex;flex-direction:column;min-width:0;flex:1}
.gs-name{color:#fff;font-weight:600;font-size:.88rem;line-height:1.3}
.gs-role{color:var(--gold-deep);font-size:.66rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-top:3px}
.gs-go{color:var(--gold);font-weight:800;flex:none}
.ra-filters{display:flex;gap:.6rem;flex-wrap:wrap;margin-top:1.6rem}
.ra-filter{background:rgba(255,255,255,.03);border:1px solid var(--line);color:var(--muted);border-radius:999px;padding:.5rem 1.1rem;font:inherit;font-size:.8rem;font-weight:700;cursor:none;transition:.25s}
@media(hover:none){.ra-filter{cursor:pointer}}
.ra-filter:hover{border-color:var(--line-gold);color:var(--gold-soft)}
.ra-filter.is-on{background:linear-gradient(135deg,var(--gold-soft),var(--gold));color:#1a0a0e;border-color:transparent}
.pub-card.is-hidden{display:none}
@media(max-width:900px){.ra-kpis{grid-template-columns:repeat(2,1fr)}.ra-charts{grid-template-columns:1fr}}
'''

js=f'''
/* ===== RESEARCH ANALYTICS CHARTS ===== */
(function(){{
  var SC={sc}, NS={ns}, TOT={len(pubs)};
  var DATA=[{bars}];
  var drawn=false;

  function donut(){{
    var svg=document.getElementById('raDonut'); if(!svg)return;
    var cx=110,cy=110,r=78,w=26, C=2*Math.PI*r;
    var parts=[{{v:SC,c:'url(#gSc)'}},{{v:NS,c:'url(#gNs)'}}];
    var html='<defs>'+
      '<linearGradient id="gSc" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f59a4e"/><stop offset="1" stop-color="#e9711c"/></linearGradient>'+
      '<linearGradient id="gNs" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#a52338"/><stop offset="1" stop-color="#6b1320"/></linearGradient></defs>';
    html+='<circle cx="'+cx+'" cy="'+cy+'" r="'+r+'" fill="none" stroke="rgba(255,255,255,.06)" stroke-width="'+w+'"/>';
    var off=0;
    parts.forEach(function(p,i){{
      var len=C*(p.v/TOT);
      html+='<circle class="raSeg" cx="'+cx+'" cy="'+cy+'" r="'+r+'" fill="none" stroke="'+p.c+'" stroke-width="'+w+'"'+
        ' stroke-linecap="butt" stroke-dasharray="0 '+C+'" transform="rotate(-90 '+cx+' '+cy+')"'+
        ' data-len="'+len+'" data-off="'+(-off)+'" style="transition:stroke-dasharray 1.1s cubic-bezier(.2,.8,.2,1) '+(i*.18)+'s"/>';
      off+=len;
    }});
    html+='<text x="'+cx+'" y="'+(cy-4)+'" text-anchor="middle" fill="#f2b705" style="font:700 30px \\'Space Grotesk\\',sans-serif">'+TOT+'</text>';
    html+='<text x="'+cx+'" y="'+(cy+18)+'" text-anchor="middle" fill="#b3a39c" style="font:600 10px Inter,sans-serif;letter-spacing:1.6px">PAPERS</text>';
    svg.innerHTML=html;
    requestAnimationFrame(function(){{
      svg.querySelectorAll('.raSeg').forEach(function(s){{
        s.setAttribute('stroke-dasharray',s.dataset.len+' '+(C-s.dataset.len));
        s.setAttribute('stroke-dashoffset',s.dataset.off);
      }});
    }});
  }}

  function bars(){{
    var svg=document.getElementById('raBars'); if(!svg)return;
    var W=560,H=300,L=42,R=14,T=18,B=42;
    var iw=W-L-R, ih=H-T-B;
    var max=Math.max.apply(null,DATA.map(function(d){{return d.n}}))||1;
    max=Math.ceil(max/2)*2;
    var n=DATA.length, slot=iw/n, bw=Math.min(46,slot*.56);
    var h='<defs><linearGradient id="gBar" x1="0" y1="1" x2="0" y2="0">'+
      '<stop offset="0" stop-color="#6b1320"/><stop offset="1" stop-color="#f2b705"/></linearGradient></defs>';
    for(var g=0;g<=max;g+=Math.max(1,max/4)){{
      var y=T+ih-(g/max)*ih;
      h+='<line x1="'+L+'" y1="'+y+'" x2="'+(W-R)+'" y2="'+y+'" stroke="rgba(255,255,255,.07)" stroke-width="1"/>';
      h+='<text x="'+(L-9)+'" y="'+(y+4)+'" text-anchor="end" fill="#80706a" style="font:600 10px Inter,sans-serif">'+Math.round(g)+'</text>';
    }}
    var pts=[];
    DATA.forEach(function(d,i){{
      var cx=L+slot*i+slot/2, bh=(d.n/max)*ih, y=T+ih-bh;
      pts.push([cx,y]);
      h+='<rect class="raBar" x="'+(cx-bw/2)+'" y="'+(T+ih)+'" width="'+bw+'" height="0" rx="5" fill="url(#gBar)"'+
         ' data-y="'+y+'" data-h="'+bh+'" style="transition:y .9s cubic-bezier(.2,.8,.2,1) '+(i*.07)+'s,height .9s cubic-bezier(.2,.8,.2,1) '+(i*.07)+'s"><title>'+d.y+': '+d.n+'</title></rect>';
      h+='<text x="'+cx+'" y="'+(T+ih+18)+'" text-anchor="middle" fill="#b3a39c" style="font:700 10px Inter,sans-serif">'+d.y+'</text>';
      h+='<text class="raVal" x="'+cx+'" y="'+(y-7)+'" text-anchor="middle" fill="#ffd95e" opacity="0" style="font:700 11px \\'Space Grotesk\\',sans-serif;transition:opacity .5s '+(0.5+i*.07)+'s">'+d.n+'</text>';
    }});
    var dstr=pts.map(function(p,i){{return (i?'L':'M')+p[0]+' '+p[1]}}).join(' ');
    h+='<path class="raLine" d="'+dstr+'" fill="none" stroke="#ffd95e" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round" opacity=".85" stroke-dasharray="1400" stroke-dashoffset="1400" style="transition:stroke-dashoffset 1.5s ease .5s"/>';
    pts.forEach(function(p,i){{
      h+='<circle class="raDotC" cx="'+p[0]+'" cy="'+p[1]+'" r="3.6" fill="#0a0608" stroke="#ffd95e" stroke-width="2" opacity="0" style="transition:opacity .4s '+(0.7+i*.07)+'s"/>';
    }});
    svg.innerHTML=h;
    requestAnimationFrame(function(){{
      svg.querySelectorAll('.raBar').forEach(function(b){{b.setAttribute('y',b.dataset.y);b.setAttribute('height',b.dataset.h);}});
      svg.querySelectorAll('.raVal,.raDotC').forEach(function(e){{e.setAttribute('opacity',e.classList.contains('raVal')?'1':'1');}});
      var ln=svg.querySelector('.raLine'); if(ln)ln.setAttribute('stroke-dashoffset','0');
    }});
  }}

  function counters(){{
    document.querySelectorAll('.ra-num').forEach(function(el){{
      var end=+el.dataset.count,st=null,dur=1100;
      function step(ts){{ if(!st)st=ts; var p=Math.min((ts-st)/dur,1);
        el.textContent=Math.round(end*(1-Math.pow(1-p,3)));
        if(p<1)requestAnimationFrame(step); }}
      requestAnimationFrame(step);
    }});
  }}

  function boot(){{ if(drawn)return; drawn=true; donut(); bars(); counters(); }}

  var sec=document.getElementById('publications');
  if('IntersectionObserver' in window && sec){{
    var io=new IntersectionObserver(function(es){{
      es.forEach(function(e){{ if(e.isIntersecting){{ boot(); io.disconnect(); }} }});
    }},{{threshold:.12}});
    io.observe(sec);
  }} else {{ boot(); }}
  setTimeout(boot,2600);

  /* filters */
  document.querySelectorAll('.ra-filter').forEach(function(btn){{
    btn.addEventListener('click',function(){{
      var f=btn.dataset.filter;
      document.querySelectorAll('.ra-filter').forEach(function(b){{b.classList.toggle('is-on',b===btn)}});
      document.querySelectorAll('#pubList .pub-card').forEach(function(c){{
        var isS=c.dataset.scopus==='true';
        c.classList.toggle('is-hidden', f==='scopus'?!isS : f==='non'?isS : false);
      }});
    }});
  }});
}})();
'''

open('research-section.html','w').write(html)
open('research-analytics.css','w').write(css)
open('research-analytics.js','w').write(js)
print("section",len(html),"css",len(css),"js",len(js))
