
/* ===== RESEARCH ANALYTICS CHARTS ===== */
(function(){
  var SC=9, NS=11, TOT=20;
  var DATA=[{y:2010,n:1},{y:2018,n:1},{y:2022,n:1},{y:2023,n:4},{y:2024,n:2},{y:2025,n:4},{y:2026,n:7},];
  var drawn=false;

  function donut(){
    var svg=document.getElementById('raDonut'); if(!svg)return;
    var cx=110,cy=110,r=78,w=26, C=2*Math.PI*r;
    var parts=[{v:SC,c:'url(#gSc)'},{v:NS,c:'url(#gNs)'}];
    var html='<defs>'+
      '<linearGradient id="gSc" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f59a4e"/><stop offset="1" stop-color="#e9711c"/></linearGradient>'+
      '<linearGradient id="gNs" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#a52338"/><stop offset="1" stop-color="#6b1320"/></linearGradient></defs>';
    html+='<circle cx="'+cx+'" cy="'+cy+'" r="'+r+'" fill="none" stroke="rgba(255,255,255,.06)" stroke-width="'+w+'"/>';
    var off=0;
    parts.forEach(function(p,i){
      var len=C*(p.v/TOT);
      html+='<circle class="raSeg" cx="'+cx+'" cy="'+cy+'" r="'+r+'" fill="none" stroke="'+p.c+'" stroke-width="'+w+'"'+
        ' stroke-linecap="butt" stroke-dasharray="0 '+C+'" transform="rotate(-90 '+cx+' '+cy+')"'+
        ' data-len="'+len+'" data-off="'+(-off)+'" style="transition:stroke-dasharray 1.1s cubic-bezier(.2,.8,.2,1) '+(i*.18)+'s"/>';
      off+=len;
    });
    html+='<text x="'+cx+'" y="'+(cy-4)+'" text-anchor="middle" fill="#f2b705" style="font:700 30px \'Space Grotesk\',sans-serif">'+TOT+'</text>';
    html+='<text x="'+cx+'" y="'+(cy+18)+'" text-anchor="middle" fill="#b3a39c" style="font:600 10px Inter,sans-serif;letter-spacing:1.6px">PAPERS</text>';
    svg.innerHTML=html;
    requestAnimationFrame(function(){
      svg.querySelectorAll('.raSeg').forEach(function(s){
        s.setAttribute('stroke-dasharray',s.dataset.len+' '+(C-s.dataset.len));
        s.setAttribute('stroke-dashoffset',s.dataset.off);
      });
    });
  }

  function bars(){
    var svg=document.getElementById('raBars'); if(!svg)return;
    var W=560,H=300,L=42,R=14,T=18,B=42;
    var iw=W-L-R, ih=H-T-B;
    var max=Math.max.apply(null,DATA.map(function(d){return d.n}))||1;
    max=Math.ceil(max/2)*2;
    var n=DATA.length, slot=iw/n, bw=Math.min(46,slot*.56);
    var h='<defs><linearGradient id="gBar" x1="0" y1="1" x2="0" y2="0">'+
      '<stop offset="0" stop-color="#6b1320"/><stop offset="1" stop-color="#f2b705"/></linearGradient></defs>';
    for(var g=0;g<=max;g+=Math.max(1,max/4)){
      var y=T+ih-(g/max)*ih;
      h+='<line x1="'+L+'" y1="'+y+'" x2="'+(W-R)+'" y2="'+y+'" stroke="rgba(255,255,255,.07)" stroke-width="1"/>';
      h+='<text x="'+(L-9)+'" y="'+(y+4)+'" text-anchor="end" fill="#80706a" style="font:600 10px Inter,sans-serif">'+Math.round(g)+'</text>';
    }
    var pts=[];
    DATA.forEach(function(d,i){
      var cx=L+slot*i+slot/2, bh=(d.n/max)*ih, y=T+ih-bh;
      pts.push([cx,y]);
      h+='<rect class="raBar" x="'+(cx-bw/2)+'" y="'+(T+ih)+'" width="'+bw+'" height="0" rx="5" fill="url(#gBar)"'+
         ' data-y="'+y+'" data-h="'+bh+'" style="transition:y .9s cubic-bezier(.2,.8,.2,1) '+(i*.07)+'s,height .9s cubic-bezier(.2,.8,.2,1) '+(i*.07)+'s"><title>'+d.y+': '+d.n+'</title></rect>';
      h+='<text x="'+cx+'" y="'+(T+ih+18)+'" text-anchor="middle" fill="#b3a39c" style="font:700 10px Inter,sans-serif">'+d.y+'</text>';
      h+='<text class="raVal" x="'+cx+'" y="'+(y-7)+'" text-anchor="middle" fill="#ffd95e" opacity="0" style="font:700 11px \'Space Grotesk\',sans-serif;transition:opacity .5s '+(0.5+i*.07)+'s">'+d.n+'</text>';
    });
    var dstr=pts.map(function(p,i){return (i?'L':'M')+p[0]+' '+p[1]}).join(' ');
    h+='<path class="raLine" d="'+dstr+'" fill="none" stroke="#ffd95e" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round" opacity=".85" stroke-dasharray="1400" stroke-dashoffset="1400" style="transition:stroke-dashoffset 1.5s ease .5s"/>';
    pts.forEach(function(p,i){
      h+='<circle class="raDotC" cx="'+p[0]+'" cy="'+p[1]+'" r="3.6" fill="#0a0608" stroke="#ffd95e" stroke-width="2" opacity="0" style="transition:opacity .4s '+(0.7+i*.07)+'s"/>';
    });
    svg.innerHTML=h;
    requestAnimationFrame(function(){
      svg.querySelectorAll('.raBar').forEach(function(b){b.setAttribute('y',b.dataset.y);b.setAttribute('height',b.dataset.h);});
      svg.querySelectorAll('.raVal,.raDotC').forEach(function(e){e.setAttribute('opacity',e.classList.contains('raVal')?'1':'1');});
      var ln=svg.querySelector('.raLine'); if(ln)ln.setAttribute('stroke-dashoffset','0');
    });
  }

  function counters(){
    document.querySelectorAll('.ra-num').forEach(function(el){
      var end=+el.dataset.count,st=null,dur=1100;
      function step(ts){ if(!st)st=ts; var p=Math.min((ts-st)/dur,1);
        el.textContent=Math.round(end*(1-Math.pow(1-p,3)));
        if(p<1)requestAnimationFrame(step); }
      requestAnimationFrame(step);
    });
  }

  function boot(){ if(drawn)return; drawn=true; donut(); bars(); counters(); }

  var sec=document.getElementById('publications');
  if('IntersectionObserver' in window && sec){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ boot(); io.disconnect(); } });
    },{threshold:.12});
    io.observe(sec);
  } else { boot(); }
  setTimeout(boot,2600);

  /* filters */
  document.querySelectorAll('.ra-filter').forEach(function(btn){
    btn.addEventListener('click',function(){
      var f=btn.dataset.filter;
      document.querySelectorAll('.ra-filter').forEach(function(b){b.classList.toggle('is-on',b===btn)});
      document.querySelectorAll('#pubList .pub-card').forEach(function(c){
        var isS=c.dataset.scopus==='true';
        c.classList.toggle('is-hidden', f==='scopus'?!isS : f==='non'?isS : false);
      });
    });
  });
})();
