
import json
import os

import streamlit as st
import streamlit.components.v1 as components

# --------------------------------------------------------------------------
# CONFIGURATION
# --------------------------------------------------------------------------


def _cfg(key: str, default: str = "") -> str:
    """Read config from st.secrets, then environment, then default."""
    try:
        if key in st.secrets:
            return str(st.secrets[key])
    except Exception:
        pass
    return os.environ.get(key, default)


MAPS_URL = "https://maps.app.goo.gl/Sq2HDYSHddsj9Tb1A"  # e.g. "https://maps.app.goo.gl/xxxxxxxx"
SITE_URL = _cfg("SITE_URL", "")  # e.g. "https://keshav-anila.streamlit.app"

GROOM_NAME = "Keshav"
BRIDE_NAME = "Anila"

# Put the parents' names here exactly as they should appear, e.g.
#   "Son of Mr. ___ & Mrs. ___ Bhardwaj"
# While empty, a neutral family line is shown instead (nothing is invented).
GROOM_PARENTS = _cfg("GROOM_PARENTS", "")
BRIDE_PARENTS = _cfg("BRIDE_PARENTS", "")

CONFIG = {
    "mapsUrl": MAPS_URL.strip(),
    "siteUrl": SITE_URL.strip(),
    "groom": GROOM_NAME,
    "bride": BRIDE_NAME,
    "groomParents": GROOM_PARENTS.strip() or "S/O Mrs.Sunita bhardwaj & Mr.Vijender Kumar Bhardwaj",
    "brideParents": BRIDE_PARENTS.strip() or "D/O Mrs.Sonia & Mr.Deepak",
    # Countdown target: start of 5 Dec 2026, India Standard Time
    "target": "2026-12-05T00:00:00+05:30",
}

# --------------------------------------------------------------------------
# PAGE HTML (CSS + HTML + JS in one self-contained document)
# --------------------------------------------------------------------------

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Keshav &amp; Anila - Wedding Invitation</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@400;700&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Great+Vibes&display=swap" rel="stylesheet">
<style>
:root{
  --maroon:#5e0b17; --maroon-d:#3f070f; --maroon-l:#86182a;
  --ivory:#fbf3e4; --ivory-d:#f1e4c8;
  --gold:#c9a24b; --gold-l:#e8cd87; --gold-d:#9c7a2c;
  --night:#0b1236; --night-2:#1a2557;
  --serif:'Cormorant Garamond',Georgia,'Times New Roman',serif;
  --display:'Cinzel Decorative','Cormorant Garamond',Georgia,serif;
  --script:'Great Vibes','Cormorant Garamond',cursive;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{font-family:var(--serif);color:var(--maroon-d);background:var(--ivory);
  overflow-x:hidden;font-size:19px;line-height:1.6}
img,svg{max-width:100%}
a{color:inherit}
button{font-family:inherit;cursor:pointer}
:focus-visible{outline:3px solid var(--gold-l);outline-offset:3px}

/* ---------- progress + nav ---------- */
#progress{position:fixed;top:0;left:0;height:3px;width:0;z-index:60;
  background:linear-gradient(90deg,var(--gold-d),var(--gold-l),var(--gold-d))}
nav{position:fixed;top:3px;left:0;right:0;z-index:50;display:flex;justify-content:center;
  gap:clamp(.6rem,3vw,2rem);padding:.55rem 1rem;
  background:rgba(63,7,15,.82);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);
  border-bottom:1px solid rgba(201,162,75,.45);
  transform:translateY(-110%);transition:transform .4s ease}
nav.show{transform:none}
nav a{color:var(--gold-l);text-decoration:none;font-size:.82rem;letter-spacing:.18em;
  text-transform:uppercase;padding:.25rem .3rem;border-bottom:1px solid transparent}
nav a:hover,nav a.active{border-bottom-color:var(--gold-l)}
#toTop{position:fixed;right:16px;bottom:16px;z-index:55;width:46px;height:46px;border-radius:50%;
  border:1.5px solid var(--gold);background:var(--maroon);color:var(--gold-l);font-size:1.3rem;
  display:grid;place-items:center;opacity:0;pointer-events:none;transform:translateY(12px);
  transition:.3s;box-shadow:0 4px 14px rgba(0,0,0,.35)}
#toTop.show{opacity:1;pointer-events:auto;transform:none}

/* ---------- shared ---------- */
section{position:relative;padding:clamp(4.5rem,11vw,8rem) 1.25rem;text-align:center;
  min-height:80vh;display:flex;flex-direction:column;align-items:center;justify-content:center}
.wrap{width:100%;max-width:880px;margin:0 auto;position:relative;z-index:2}
.eyebrow{font-size:.85rem;letter-spacing:.38em;text-transform:uppercase;color:var(--gold-d);margin-bottom:.8rem}
h2{font-family:var(--display);font-weight:400;font-size:clamp(1.6rem,5.5vw,2.7rem);
  letter-spacing:.06em;line-height:1.25;color:var(--maroon)}
.script{font-family:var(--script);font-weight:400}
.divider{display:flex;align-items:center;justify-content:center;gap:.8rem;margin:1.4rem auto;
  color:var(--gold);max-width:340px;width:100%}
.divider::before,.divider::after{content:"";flex:1;height:1px;
  background:linear-gradient(90deg,transparent,var(--gold),transparent)}
.divider svg{width:26px;height:26px;flex:none}
.btn{display:inline-block;border:1.5px solid var(--gold);background:linear-gradient(180deg,var(--maroon-l),var(--maroon));
  color:var(--gold-l);padding:.85rem 2rem;border-radius:999px;font-size:1rem;letter-spacing:.2em;
  text-transform:uppercase;text-decoration:none;box-shadow:0 6px 18px rgba(63,7,15,.35),inset 0 0 0 3px rgba(201,162,75,.18);
  transition:transform .2s,box-shadow .2s}
.btn:hover{transform:translateY(-2px);box-shadow:0 10px 22px rgba(63,7,15,.4),inset 0 0 0 3px rgba(201,162,75,.3)}
.btn.light{background:linear-gradient(180deg,var(--gold-l),var(--gold));color:var(--maroon-d);border-color:var(--gold-d)}
.btn[aria-disabled="true"]{opacity:.55;pointer-events:none;filter:grayscale(.3)}
.border-orn{position:absolute;inset:12px;border:1.5px solid var(--gold);pointer-events:none;z-index:1;opacity:.75}
.border-orn::after{content:"";position:absolute;inset:6px;border:1px solid var(--gold);opacity:.6}
.corner{position:absolute;width:64px;height:64px;color:var(--gold);z-index:2;opacity:.9}
.corner.tl{top:6px;left:6px}.corner.tr{top:6px;right:6px;transform:scaleX(-1)}
.corner.bl{bottom:6px;left:6px;transform:scaleY(-1)}.corner.br{bottom:6px;right:6px;transform:scale(-1,-1)}

/* reveal on scroll */
.reveal{opacity:0;transform:translateY(26px);transition:opacity .9s ease,transform .9s ease}
.reveal.in{opacity:1;transform:none}
.d1{transition-delay:.12s}.d2{transition-delay:.24s}.d3{transition-delay:.36s}
.no-io .reveal{opacity:1;transform:none}

/* ---------- 1 welcome ---------- */
#welcome{min-height:100vh;color:var(--gold-l);
  background:radial-gradient(ellipse at 50% 30%,var(--maroon-l) 0%,var(--maroon) 45%,var(--maroon-d) 100%)}
#welcome::before{content:"";position:absolute;inset:0;opacity:.12;
  background-image:radial-gradient(var(--gold) 1px,transparent 1.5px);background-size:26px 26px}
.mono{width:132px;height:132px;margin:0 auto 1.2rem;border-radius:50%;display:grid;place-items:center;
  border:2px solid var(--gold);box-shadow:0 0 0 6px rgba(201,162,75,.18),0 0 40px rgba(232,205,135,.25);
  font-family:var(--display);font-size:2rem;color:var(--gold-l);letter-spacing:.05em;
  background:radial-gradient(circle,rgba(0,0,0,.2),transparent)}
.mono small{font-size:1.1rem;margin:0 .15rem;color:var(--gold)}
#welcome .pre{letter-spacing:.35em;text-transform:uppercase;font-size:.85rem;color:var(--gold)}
#welcome h1{font-family:var(--display);font-weight:400;font-size:clamp(1.7rem,7vw,3.4rem);
  line-height:1.25;margin:.8rem 0;letter-spacing:.05em;color:var(--ivory)}
#welcome h1 .amp{display:block;font-family:var(--script);font-size:1.3em;color:var(--gold);line-height:1.1}
#welcome .sub{font-style:italic;color:var(--gold-l);margin-bottom:1.8rem}
#openMsg{max-height:0;overflow:hidden;opacity:0;transition:max-height .8s ease,opacity .8s ease,margin .8s;margin-top:0}
#openMsg.show{max-height:260px;opacity:1;margin-top:1.8rem}
#openMsg p{font-family:var(--script);font-size:clamp(1.6rem,5vw,2.2rem);color:var(--gold-l)}
.scroll-cue{display:inline-flex;flex-direction:column;align-items:center;gap:.3rem;margin-top:.7rem;
  background:none;border:0;color:var(--gold);font-size:.8rem;letter-spacing:.3em;text-transform:uppercase;text-decoration:none}
.scroll-cue span{display:block;width:18px;height:18px;border-right:2px solid var(--gold);
  border-bottom:2px solid var(--gold);transform:rotate(45deg);animation:bob 1.6s infinite}
@keyframes bob{0%,100%{transform:translateY(0) rotate(45deg)}50%{transform:translateY(7px) rotate(45deg)}}

/* ---------- 2 families ---------- */
#families{background:var(--ivory);
  background-image:radial-gradient(circle at 50% 0,var(--ivory-d),transparent 60%)}
.fam-grid{display:grid;gap:2.2rem;margin-top:2rem}
.fam h3{font-family:var(--display);font-weight:400;font-size:clamp(1.4rem,5vw,2.2rem);color:var(--maroon);letter-spacing:.05em}
.fam .rel{font-style:italic;font-size:1.15rem;color:var(--gold-d);margin-top:.35rem}
.fam .tag{font-size:.8rem;letter-spacing:.3em;text-transform:uppercase;color:var(--gold-d);margin-bottom:.4rem}
.weds{font-family:var(--script);font-size:2.6rem;color:var(--gold-d);line-height:1}
.invite-line{max-width:560px;margin:0 auto;font-style:italic}
@media(min-width:760px){.fam-grid{grid-template-columns:1fr auto 1fr;align-items:center}}

/* ---------- 3 date reveal ---------- */
#date{background:linear-gradient(180deg,var(--maroon-d),var(--maroon) 50%,var(--maroon-d));color:var(--gold-l);overflow:hidden}
#date h2{color:var(--gold-l)}
#date .eyebrow{color:var(--gold)}
.seal-btn{margin:2rem auto 1rem;background:none;border:0;display:block;position:relative;transition:transform .3s}
.seal-btn:hover{transform:scale(1.05)}
.seal{width:176px;height:176px;border-radius:50%;display:grid;place-items:center;position:relative;
  background:radial-gradient(circle at 35% 30%,var(--gold-l),var(--gold) 55%,var(--gold-d));
  box-shadow:0 0 0 8px rgba(201,162,75,.25),0 12px 30px rgba(0,0,0,.5);animation:pulse 2.6s infinite}
.seal::before{content:"";position:absolute;inset:10px;border-radius:50%;border:2px dashed var(--maroon-d);opacity:.6}
.seal b{font-family:var(--display);font-size:2rem;color:var(--maroon-d);font-weight:700}
@keyframes pulse{0%,100%{box-shadow:0 0 0 8px rgba(201,162,75,.25),0 12px 30px rgba(0,0,0,.5)}
  50%{box-shadow:0 0 0 18px rgba(201,162,75,.08),0 0 50px rgba(232,205,135,.55)}}
.hint{font-size:.85rem;letter-spacing:.28em;text-transform:uppercase;color:var(--gold)}
#dateReveal{max-height:0;opacity:0;overflow:hidden;transition:max-height 1s ease,opacity 1s ease;position:relative}
#dateReveal.show{max-height:380px;opacity:1}
#dateReveal .big{font-family:var(--display);font-size:clamp(2.2rem,10vw,5rem);color:var(--gold-l);
  letter-spacing:.08em;line-height:1.1;text-shadow:0 0 28px rgba(232,205,135,.7);margin:.5rem 0}
#dateReveal .dow{font-family:var(--script);font-size:2.2rem;color:var(--gold)}
.sparkle{position:absolute;width:8px;height:8px;pointer-events:none;border-radius:50%;
  background:radial-gradient(circle,#fff,var(--gold-l) 50%,transparent 70%);animation:spark 1.4s ease-out forwards}
@keyframes spark{0%{opacity:1;transform:translate(0,0) scale(1)}100%{opacity:0;transform:translate(var(--dx),var(--dy)) scale(.2)}}
.glow{animation:glow 1.6s ease-out}
@keyframes glow{0%{filter:brightness(2.2)}100%{filter:none}}

/* ---------- 4 countdown ---------- */
#countdown{background:var(--ivory);
  background-image:linear-gradient(rgba(251,243,228,.93),rgba(251,243,228,.93)),
  radial-gradient(var(--gold) 1px,transparent 1.5px);background-size:auto,22px 22px}
.cd{display:grid;grid-template-columns:repeat(4,1fr);gap:clamp(.5rem,2.5vw,1.2rem);margin-top:2rem}
.cd div{background:linear-gradient(180deg,var(--maroon-l),var(--maroon-d));color:var(--gold-l);
  border:1.5px solid var(--gold);border-radius:14px;padding:1rem .2rem;
  box-shadow:0 6px 16px rgba(63,7,15,.3),inset 0 0 0 3px rgba(201,162,75,.15)}
.cd b{display:block;font-family:var(--display);font-size:clamp(1.5rem,7vw,3rem);font-weight:700;line-height:1.1;font-variant-numeric:tabular-nums}
.cd span{font-size:clamp(.6rem,2.4vw,.82rem);letter-spacing:.2em;text-transform:uppercase;color:var(--gold)}
#cdNote{margin-top:1.4rem;font-style:italic;color:var(--gold-d)}

/* ---------- 5 timeline ---------- */
#events{background:linear-gradient(180deg,var(--ivory-d),var(--ivory));justify-content:flex-start}
.timeline{position:relative;margin-top:2.5rem;padding:0 0 0 0;display:grid;gap:2.4rem;text-align:left}
.timeline::before{content:"";position:absolute;left:21px;top:10px;bottom:10px;width:3px;border-radius:3px;
  background:linear-gradient(180deg,var(--gold-l),var(--gold),var(--gold-d))}
.ev{position:relative;padding-left:58px}
.ev .node{position:absolute;left:8px;top:22px;width:30px;height:30px;border-radius:50%;
  background:var(--ivory);border:3px solid var(--gold);box-shadow:0 0 0 5px rgba(201,162,75,.2);display:grid;place-items:center;color:var(--gold-d);font-size:.8rem}
.card{border-radius:18px;overflow:hidden;border:1.5px solid var(--gold);box-shadow:0 10px 26px rgba(63,7,15,.22)}
.card .art{height:150px;display:grid;place-items:center;position:relative;overflow:hidden}
.card .art svg{position:absolute;inset:0;width:100%;height:100%}
.card .body{padding:1.1rem 1.3rem 1.4rem;text-align:center}
.card .time{font-size:1.35rem;letter-spacing:.3em;text-transform:uppercase}
.card h3{font-family:var(--display);font-weight:400;font-size:clamp(1.25rem,4.5vw,1.7rem);margin:.3rem 0;line-height:1.3}
.card p{font-style:italic}
.c-rec .art{background:linear-gradient(135deg,#7a1224,#a8284a)}
.c-rec .body{background:#fff7ec}.c-rec .time{color:var(--gold-d)}.c-rec h3{color:var(--maroon)}
.c-din .art{background:linear-gradient(135deg,#3a0a12,#6b1a24)}
.c-din .body{background:#fffaf1}.c-din .time{color:var(--gold-d)}.c-din h3{color:var(--maroon)}
.c-doli .art{background:linear-gradient(180deg,#050a24,var(--night-2));height:190px}
.c-doli .body{background:linear-gradient(180deg,var(--night-2),var(--night));color:var(--gold-l)}
.c-doli .time{color:var(--gold)}.c-doli h3{color:var(--gold-l)}
.twinkle{animation:tw 2.4s ease-in-out infinite}
.twinkle:nth-child(2n){animation-delay:.7s}.twinkle:nth-child(3n){animation-delay:1.3s}
@keyframes tw{0%,100%{opacity:.25}50%{opacity:1}}
@media(min-width:760px){.timeline{max-width:640px;margin-left:auto;margin-right:auto}}

/* ---------- 6 message ---------- */
#message{background:var(--ivory)}
.letter{max-width:640px;margin:1.8rem auto 0;padding:2rem 1.5rem;border:1.5px solid var(--gold);
  background:linear-gradient(180deg,#fffaf0,var(--ivory));border-radius:10px;
  box-shadow:inset 0 0 0 6px var(--ivory),inset 0 0 0 7px rgba(201,162,75,.6),0 8px 22px rgba(63,7,15,.12)}
.letter p{margin-bottom:1rem}
.letter .sig{font-family:var(--script);font-size:2rem;color:var(--maroon);margin:.6rem 0 0}
.diya-wrap{margin-top:1.6rem}
.diya{background:none;border:0;display:inline-grid;justify-items:center;gap:.2rem;color:var(--maroon)}
.diya svg{width:92px;height:92px;overflow:visible}
.flame{transform-origin:50% 100%;transform-box:fill-box;animation:flick 1.8s ease-in-out infinite;opacity:.25;filter:grayscale(1)}
.diya.lit .flame{opacity:1;filter:none}
@keyframes flick{0%,100%{transform:scale(1,1)}50%{transform:scale(.92,1.1) rotate(2deg)}}
.diya.lit svg{filter:drop-shadow(0 0 14px rgba(255,190,70,.9))}
#blessing{min-height:2.4rem;font-family:var(--script);font-size:1.7rem;color:var(--gold-d);margin-top:.6rem}

/* ---------- 7 love ---------- */
#love{background:linear-gradient(180deg,var(--ivory),var(--ivory-d));overflow:hidden}
.floral{width:min(420px,90%);margin:1rem auto;display:block}
.gallery{display:grid;grid-template-columns:repeat(3,1fr);gap:.7rem;max-width:560px;margin:1.6rem auto 0}
.gallery .ph{aspect-ratio:3/4;border-radius:10px;border:1.5px solid var(--gold);
  background:linear-gradient(160deg,var(--maroon-l),var(--maroon-d));display:grid;place-items:center;
  color:var(--gold-l);overflow:hidden}
.gallery .ph img{width:100%;height:100%;object-fit:cover}
.gallery .ph svg{width:55%;opacity:.85}
.note-small{font-size:.9rem;font-style:italic;color:var(--gold-d);margin-top:.9rem}

/* ---------- 8 save the date ---------- */
#save{background:linear-gradient(180deg,var(--maroon),var(--maroon-d));color:var(--gold-l)}
#save h2{color:var(--gold-l)}
.actions{display:flex;flex-wrap:wrap;gap:1rem;justify-content:center;margin-top:2rem}
.btn.wa{background:linear-gradient(180deg,#2fbf5f,#1c8f44);color:#fff;border-color:#a6efc0}
#saveMsg{margin-top:1.2rem;min-height:1.6rem;font-style:italic;color:var(--gold)}

/* ---------- 9 location ---------- */
#location{background:var(--ivory);background-image:radial-gradient(circle at 50% 100%,var(--ivory-d),transparent 65%)}
.final-inv{font-family:var(--script);font-size:clamp(2rem,7vw,3.2rem);color:var(--maroon);line-height:1.2;margin:1rem 0}
#locNote{margin-top:1rem;font-style:italic;color:var(--gold-d)}
.btn.big{font-size:1.05rem;padding:1.05rem 2.4rem}

/* ---------- 10 finale ---------- */
#finale{min-height:100vh;color:var(--gold-l);overflow:hidden;
  background:radial-gradient(ellipse at 50% 20%,var(--night-2),var(--night) 55%,#04071c)}
#stars{position:absolute;inset:0;z-index:1}
#stars i{position:absolute;width:3px;height:3px;border-radius:50%;background:var(--gold-l);animation:tw 3s ease-in-out infinite}
#finale .date-f{font-family:var(--display);font-size:clamp(1.6rem,7vw,3rem);letter-spacing:.12em;color:var(--gold-l);margin:1rem 0;text-shadow:0 0 22px rgba(232,205,135,.5)}
#finale .gift{font-family:var(--script);font-size:clamp(2rem,8vw,3.6rem);color:var(--ivory);margin:1.2rem 0;line-height:1.2}
#finale .sign{font-style:italic;font-size:1.15rem;color:var(--gold-l)}
#finale .sign b{display:block;font-family:var(--display);font-weight:400;font-size:1rem;letter-spacing:.14em;margin-top:.4rem;color:var(--gold)}
.flower-row{display:flex;justify-content:center;gap:1.2rem;color:var(--gold);margin:.6rem 0}
.flower-row svg{width:34px;height:34px}

@media(max-width:480px){body{font-size:17px}.corner{width:46px;height:46px}
  nav a{font-size:.7rem;letter-spacing:.1em}.seal{width:150px;height:150px}.mono{width:112px;height:112px;font-size:1.7rem}}
@media(prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  *,*::before,*::after{animation-duration:.001s!important;animation-iteration-count:1!important;transition-duration:.001s!important}
  .reveal{opacity:1;transform:none}
}
</style>
</head>
<body>
<div id="progress" aria-hidden="true"></div>
<nav id="nav" aria-label="Section navigation">
  <a href="#families" data-t="families">Families</a>
  <a href="#date" data-t="date">Date</a>
  <a href="#events" data-t="events">Events</a>
  <a href="#location" data-t="location">Location</a>
</nav>
<button id="toTop" type="button" aria-label="Back to top">&#8593;</button>

<!-- SVG symbol library -->
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <defs>
    <symbol id="corner" viewBox="0 0 64 64"><g fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round">
      <path d="M4 60V18C4 10 10 4 18 4h42"/><path d="M12 60V24c0-7 5-12 12-12h36" opacity=".6"/>
      <circle cx="22" cy="22" r="6"/><circle cx="22" cy="22" r="2" fill="currentColor"/>
      <path d="M22 10c3 4 3 8 0 12M10 22c4-3 8-3 12 0" opacity=".7"/></g></symbol>
    <symbol id="lotus" viewBox="0 0 40 40"><g fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round">
      <path d="M20 6c5 6 5 14 0 20-5-6-5-14 0-20z"/><path d="M8 14c8 0 13 6 12 12-8 0-13-5-12-12z"/>
      <path d="M32 14c-8 0-13 6-12 12 8 0 13-5 12-12z"/><path d="M10 30c6 3 14 3 20 0" /></g></symbol>
    <symbol id="flower" viewBox="0 0 40 40"><g fill="none" stroke="currentColor" stroke-width="1.5">
      <circle cx="20" cy="20" r="4" fill="currentColor"/>
      <ellipse cx="20" cy="9" rx="4" ry="7"/><ellipse cx="20" cy="31" rx="4" ry="7"/>
      <ellipse cx="9" cy="20" rx="7" ry="4"/><ellipse cx="31" cy="20" rx="7" ry="4"/>
      <ellipse cx="12" cy="12" rx="3.5" ry="6" transform="rotate(-45 12 12)"/>
      <ellipse cx="28" cy="28" rx="3.5" ry="6" transform="rotate(-45 28 28)"/>
      <ellipse cx="28" cy="12" rx="3.5" ry="6" transform="rotate(45 28 12)"/>
      <ellipse cx="12" cy="28" rx="3.5" ry="6" transform="rotate(45 12 28)"/></g></symbol>
    <symbol id="star4" viewBox="0 0 20 20"><path d="M10 0c1 6 4 9 10 10-6 1-9 4-10 10-1-6-4-9-10-10 6-1 9-4 10-10z" fill="currentColor"/></symbol>
  </defs>
</svg>

<!-- 1. ROYAL WELCOME -->
<section id="welcome">
  <div class="border-orn"></div>
  <svg class="corner tl"><use href="#corner"/></svg><svg class="corner tr"><use href="#corner"/></svg>
  <svg class="corner bl"><use href="#corner"/></svg><svg class="corner br"><use href="#corner"/></svg>
  <div class="wrap">
    <div class="mono reveal" aria-label="K and A monogram">K<small>&times;</small>A</div>
    <p class="pre reveal d1">Together with their families</p>
    <h1 class="reveal d2"><span id="gName"></span><span class="amp">&amp;</span><span id="bName"></span></h1>
    <p class="sub reveal d3">request the pleasure of your company</p>
    <button class="btn light reveal d3" id="openBtn" type="button">Open the Invitation</button>
    <div id="openMsg" aria-live="polite">
      <p>Come, celebrate with us&hellip;</p>
      <a class="scroll-cue" href="#families" data-t="families">Scroll to discover<span></span></a>
    </div>
  </div>
</section>

<!-- 2. FAMILIES -->
<section id="families">
  <div class="wrap">
    <p class="eyebrow reveal">With the blessings of our elders</p>
    <h2 class="reveal d1">The Families</h2>
    <div class="divider reveal"><svg><use href="#lotus"/></svg></div>
    <div class="fam-grid">
      <div class="fam reveal">
        <p class="tag">The Groom</p>
        <h3 id="fGroom"></h3>
        <p class="rel" id="fGroomP"></p>
      </div>
      <div class="weds reveal d1">weds</div>
      <div class="fam reveal d2">
        <p class="tag">The Bride</p>
        <h3 id="fBride"></h3>
        <p class="rel" id="fBrideP"></p>
      </div>
    </div>
    <div class="divider reveal" style="margin-top:2.4rem"><svg><use href="#flower"/></svg></div>
    <p class="invite-line reveal">Two hearts, two families, one beautiful beginning. We joyfully invite you to bless the couple.</p>
  </div>
</section>

<!-- 3. DATE REVEAL -->
<section id="date">
  <div class="wrap">
    <p class="eyebrow reveal">A date to remember</p>
    <h2 class="reveal d1">The Grand Date Reveal</h2>
    <button class="seal-btn reveal d2" id="sealBtn" type="button" aria-expanded="false" aria-controls="dateReveal">
      <div class="seal"><b>K&nbsp;&times;&nbsp;A</b></div>
    </button>
    <p class="hint" id="sealHint">Tap the golden seal</p>
    <div id="dateReveal" aria-live="polite">
      <div class="dow">Save the date</div>
      <div class="big" id="bigDate">05 DECEMBER 2026</div>
      <div class="divider"><svg><use href="#star4"/></svg></div>
    </div>
  </div>
</section>

<!-- 4. COUNTDOWN -->
<section id="countdown">
  <div class="wrap">
    <p class="eyebrow reveal">Every moment brings us closer</p>
    <h2 class="reveal d1">Our Wedding Countdown</h2>
    <div class="cd reveal d2" role="timer" aria-label="Countdown to 5 December 2026">
      <div><b id="cdD">00</b><span>Days</span></div>
      <div><b id="cdH">00</b><span>Hours</span></div>
      <div><b id="cdM">00</b><span>Minutes</span></div>
      <div><b id="cdS">00</b><span>Seconds</span></div>
    </div>
    <p id="cdNote" class="reveal d3">Counting down to 5 December 2026 (IST)</p>
  </div>
</section>

<!-- 5. TIMELINE -->
<section id="events">
  <div class="wrap">
    <p class="eyebrow reveal">The celebration</p>
    <h2 class="reveal d1">The Celebration Timeline</h2>
    <div class="timeline">
      <div class="ev reveal"><span class="node">&#10048;</span>
        <article class="card c-rec">
          <div class="art" aria-hidden="true">
            <svg viewBox="0 0 300 150" preserveAspectRatio="xMidYMid slice" style="color:#e8cd87">
              <use href="#flower" x="10" y="10" width="60" height="60"/><use href="#flower" x="230" y="70" width="64" height="64"/>
              <use href="#flower" x="120" y="55" width="62" height="62"/><use href="#lotus" x="60" y="85" width="50" height="50"/>
              <use href="#lotus" x="205" y="8" width="48" height="48"/><use href="#flower" x="268" y="6" width="26" height="26"/>
              <use href="#flower" x="6" y="108" width="30" height="30"/>
            </svg>
          </div>
          <div class="body"><div class="time">8:00 PM</div><h3>Reception of Baraat</h3><p>An evening of colour, music and togetherness.</p></div>
        </article>
      </div>
      <div class="ev reveal d1"><span class="node">&#10022;</span>
        <article class="card c-din">
          <div class="art" aria-hidden="true">
            <svg viewBox="0 0 300 150" preserveAspectRatio="xMidYMid meet" style="color:#e8cd87">
              <g fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="150" cy="78" r="38"/><circle cx="150" cy="78" r="27" opacity=".6"/>
                <path d="M92 40v30c0 6 4 9 8 9s8-3 8-9V40M100 40v82M96 40v22M104 40v22"/>
                <path d="M208 40c-8 6-10 18-10 30 0 6 4 9 8 9h2v43M208 40c4 0 6 6 6 20v19"/>
                <path d="M130 124h40" opacity=".7"/>
              </g>
              <use href="#star4" x="40" y="22" width="12" height="12" style="color:#e8cd87"/>
              <use href="#star4" x="245" y="112" width="10" height="10"/><use href="#star4" x="258" y="26" width="8" height="8"/>
            </svg>
          </div>
          <div class="body"><div class="time">9:00 PM</div><h3>Dinner</h3><p>Join us for a festive feast.</p></div>
        </article>
      </div>
      <div class="ev reveal d2"><span class="node">&#9733;</span>
        <article class="card c-doli">
          <div class="art" aria-hidden="true">
            <svg viewBox="0 0 300 190" preserveAspectRatio="xMidYMid slice" id="doliSky" style="color:#e8cd87">
              <circle cx="238" cy="46" r="20" fill="#f6e7b4"/><circle cx="246" cy="40" r="19" fill="#12195a"/>
            </svg>
          </div>
          <div class="body"><div class="time">Midnight</div><h3>Doli</h3><p>Taaron Ki Chhaon Mein</p></div>
        </article>
      </div>
    </div>
  </div>
</section>

<!-- 6. MESSAGE -->
<section id="message">
  <div class="wrap">
    <p class="eyebrow reveal">From our hearts</p>
    <h2 class="reveal d1">A Message for Our Guests</h2>
    <div class="letter reveal d2">
      <p>Every wedding is built on the love of the people who surround it. Your presence in our celebration means more to both our families than any words can carry.</p>
      <p>You have been part of our stories, our homes and our festivals. We would be truly happy to have you with us as we begin this new chapter, to share a meal, a blessing and a few joyful hours.</p>
      <p>Come as you are, bring your warmth, and stay for the celebration.</p>
      <p class="sig">The Bhardwaj &amp; Arora Families</p>
    </div>
    <div class="diya-wrap reveal d3">
      <button class="diya" id="diya" type="button" aria-label="Light the diya for a blessing">
        <svg viewBox="0 0 100 100">
          <path class="flame" d="M50 14c8 12 12 20 6 30-3 5-9 5-12 0-6-10-2-18 6-30z" fill="#ffb02e" stroke="#ff7a00" stroke-width="1.5"/>
          <path d="M14 56h72c0 18-14 30-36 30S14 74 14 56z" fill="#c9a24b" stroke="#9c7a2c" stroke-width="2"/>
          <path d="M20 56c4-5 56-5 60 0" fill="none" stroke="#9c7a2c" stroke-width="2"/>
          <rect x="47" y="40" width="6" height="14" rx="2" fill="#5e0b17"/>
        </svg>
        <small>Light the diya</small>
      </button>
      <div id="blessing" aria-live="polite"></div>
    </div>
  </div>
</section>

<!-- 7. LOVE -->
<section id="love">
  <div class="wrap">
    <p class="eyebrow reveal">Two names, one story</p>
    <h2 class="reveal d1">A Little Celebration of Love</h2>
    <div class="mono reveal d2" style="margin-top:1.4rem;color:var(--maroon);border-color:var(--gold-d);background:none;box-shadow:0 0 0 6px rgba(201,162,75,.2)">K<small style="color:var(--gold-d)">&times;</small>A</div>
    <svg class="floral reveal" viewBox="0 0 420 120" aria-hidden="true" style="color:var(--gold-d)">
      <g fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round">
        <path d="M10 70C70 30 120 100 210 62S350 30 410 70"/><path d="M10 82C70 46 120 112 210 76S350 46 410 82" opacity=".5"/>
      </g>
      <use href="#flower" x="30" y="30" width="38" height="38" style="color:var(--maroon)"/>
      <use href="#lotus" x="110" y="52" width="34" height="34"/>
      <use href="#flower" x="190" y="26" width="44" height="44" style="color:var(--maroon)"/>
      <use href="#lotus" x="276" y="52" width="34" height="34"/>
      <use href="#flower" x="352" y="30" width="38" height="38" style="color:var(--maroon)"/>
    </svg>
    <p class="reveal" style="max-width:520px;margin:0 auto;font-style:italic">Some moments are best shared with the people we love. Thank you for being part of ours.</p>
    <!-- Optional photo gallery: add image URLs to PHOTOS in app.py. Ornamental artwork shows otherwise. -->
    <div class="gallery reveal" id="gallery"></div>
    <p class="note-small reveal" id="galleryNote"></p>
  </div>
</section>

<!-- 8. SAVE & SHARE -->
<section id="save">
  <div class="wrap">
    <p class="eyebrow reveal" style="color:var(--gold)">Mark your calendar</p>
    <h2 class="reveal d1">Save the Date &amp; Share</h2>
    <p class="reveal d2" style="margin-top:1rem;max-width:520px;margin-inline:auto">Add 5 December 2026 to your calendar and share the invitation with family and friends.</p>
    <div class="actions reveal d3">
      <button class="btn light" id="icsBtn" type="button">Add to Calendar</button>
      <button class="btn wa" id="waBtn" type="button">Share on WhatsApp</button>
    </div>
    <p id="saveMsg" aria-live="polite"></p>
  </div>
</section>

<!-- 9. LOCATION -->
<section id="location">
  <div class="border-orn"></div>
  <div class="wrap">
    <p class="eyebrow reveal">We await you</p>
    <h2 class="reveal d1">Find the Wedding Location</h2>
    <div class="divider reveal"><svg><use href="#lotus"/></svg></div>
    <p class="final-inv reveal d2">We would be honoured by your presence</p>
    <div class="reveal d3"><a class="btn big" id="mapBtn" href="#" target="_blank" rel="noopener noreferrer">Open Location in Google Maps</a></div>
    <p id="locNote"></p>
  </div>
</section>

<!-- 10. FINALE -->
<section id="finale">
  <div id="stars" aria-hidden="true"></div>
  <div class="wrap">
    <div class="flower-row reveal" aria-hidden="true"><svg><use href="#flower"/></svg><svg><use href="#lotus"/></svg><svg><use href="#flower"/></svg></div>
    <p class="eyebrow reveal" style="color:var(--gold)">The Grand Finale</p>
    <div class="date-f reveal d1">05 &middot; 12 &middot; 2026</div>
    <div class="divider reveal"><svg><use href="#star4"/></svg></div>
    <p class="gift reveal d2">Your presence is our greatest gift.</p>
    <p class="sign reveal d3">With love,<b>The Bhardwaj &amp; Arora Families</b></p>
    <div class="flower-row reveal d3" style="margin-top:1.6rem" aria-hidden="true"><svg><use href="#lotus"/></svg><svg><use href="#flower"/></svg><svg><use href="#lotus"/></svg></div>
  </div>
</section>

<script>
(function(){
  "use strict";
  var CFG = __CONFIG__;
  var PHOTOS = [];   // optional: list of image URLs, e.g. ["https://.../1.jpg"]
  var $ = function(id){return document.getElementById(id)};
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* make this iframe behave like the full page (one continuous website) */
  try{
    var f = window.frameElement;
    if(f){
      f.style.cssText = "position:fixed;top:0;left:0;width:100vw;height:100vh;height:100dvh;border:0;z-index:999999;background:#fbf3e4";
      f.setAttribute("scrolling","yes");
      f.parentElement && (f.parentElement.style.height = "0");
      window.parent.document.body.style.overflow = "hidden";
    }
  }catch(e){ /* cross-origin: stays at its normal embedded size */ }

  /* fill text from config */
  $("gName").textContent = CFG.groom; $("bName").textContent = CFG.bride;
  $("fGroom").textContent = CFG.groom; $("fBride").textContent = CFG.bride;
  $("fGroomP").textContent = CFG.groomParents; $("fBrideP").textContent = CFG.brideParents;

  /* smooth scrolling (JS fallback keeps buttons from jumping/reloading) */
  function goTo(id){
    var el = $(id); if(!el) return;
    var y = el.getBoundingClientRect().top + window.pageYOffset - (id==="welcome"?0:44);
    try{ window.scrollTo({top:y,behavior:reduce?"auto":"smooth"}); }catch(e){ window.scrollTo(0,y); }
  }
  document.addEventListener("click", function(ev){
    var a = ev.target.closest && ev.target.closest("a[data-t]");
    if(a){ ev.preventDefault(); goTo(a.getAttribute("data-t")); }
  });

  /* nav, progress, back-to-top, active link */
  var nav=$("nav"), prog=$("progress"), top=$("toTop");
  var links = [].slice.call(nav.querySelectorAll("a"));
  var secs = links.map(function(a){return $(a.getAttribute("data-t"))});
  function onScroll(){
    var y = window.pageYOffset || document.documentElement.scrollTop;
    var h = document.documentElement.scrollHeight - window.innerHeight;
    prog.style.width = (h>0 ? Math.min(100, y/h*100) : 0) + "%";
    nav.classList.toggle("show", y > window.innerHeight*0.5);
    top.classList.toggle("show", y > 500);
    var cur = -1;
    secs.forEach(function(s,i){ if(s && s.getBoundingClientRect().top < window.innerHeight*0.4) cur = i; });
    links.forEach(function(a,i){ a.classList.toggle("active", i===cur); });
  }
  window.addEventListener("scroll", onScroll, {passive:true});
  window.addEventListener("resize", onScroll);
  onScroll();
  top.addEventListener("click", function(){
    try{ window.scrollTo({top:0,behavior:reduce?"auto":"smooth"}); }catch(e){ window.scrollTo(0,0); }
  });

  /* scroll reveal */
  if("IntersectionObserver" in window){
    var io = new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add("in"); io.unobserve(e.target);} });
    },{threshold:.15, rootMargin:"0px 0px -6% 0px"});
    [].forEach.call(document.querySelectorAll(".reveal"), function(el){ io.observe(el); });
  } else { document.body.classList.add("no-io"); }

  /* 1. open invitation (never blocks scrolling) */
  $("openBtn").addEventListener("click", function(){
    $("openMsg").classList.add("show");
    this.textContent = "Invitation Opened";
    this.setAttribute("aria-disabled","true");
    burst($("welcome"), this, 18);
    setTimeout(function(){ goTo("families"); }, reduce?0:1500);
  });

  /* sparkle helper */
  function burst(container, anchor, n){
    if(reduce) return;
    var cr = container.getBoundingClientRect(), ar = anchor.getBoundingClientRect();
    var cx = ar.left - cr.left + ar.width/2, cy = ar.top - cr.top + ar.height/2;
    container.style.position = "relative";
    for(var i=0;i<n;i++){
      var s = document.createElement("span"); s.className="sparkle";
      var ang = Math.random()*Math.PI*2, d = 50+Math.random()*110;
      s.style.left = cx+"px"; s.style.top = cy+"px";
      s.style.setProperty("--dx", Math.cos(ang)*d+"px"); s.style.setProperty("--dy", Math.sin(ang)*d+"px");
      container.appendChild(s); setTimeout((function(el){return function(){el.remove()}})(s),1500);
    }
  }

  /* 3. date reveal */
  var sealBtn=$("sealBtn"), revealed=false;
  sealBtn.addEventListener("click", function(){
    var box=$("dateReveal");
    if(!revealed){
      revealed=true; box.classList.add("show","glow");
      sealBtn.setAttribute("aria-expanded","true");
      $("sealHint").textContent = "With joy, we celebrate on";
      burst($("date"), sealBtn, 30);
      setTimeout(function(){ burst($("date"), $("bigDate"), 26); }, 400);
    } else { burst($("date"), sealBtn, 14); }
  });

  /* 4. countdown (Asia/Kolkata fixed offset, never negative) */
  var target = new Date(CFG.target).getTime();
  function pad(n){return n<10?"0"+n:""+n}
  function tick(){
    var diff = Math.max(0, target - Date.now());
    var s = Math.floor(diff/1000);
    var d = Math.floor(s/86400); s -= d*86400;
    var h = Math.floor(s/3600);  s -= h*3600;
    var m = Math.floor(s/60);    s -= m*60;
    $("cdD").textContent = d<100?pad(d):d; $("cdH").textContent=pad(h);
    $("cdM").textContent=pad(m); $("cdS").textContent=pad(s);
    if(target - Date.now() <= 0){
      var end = target + 86400000;
      $("cdNote").textContent = Date.now() < end ? "Today is the day. Join us in celebration!" : "Thank you for celebrating with us.";
    }
  }
  tick(); setInterval(tick, 1000);

  /* 5. starry sky for doli */
  (function(){
    var sky=$("doliSky"), ns="http://www.w3.org/2000/svg", g=document.createElementNS(ns,"g");
    var seed=7; function rnd(){ seed=(seed*9301+49297)%233280; return seed/233280; }
    for(var i=0;i<46;i++){
      var c=document.createElementNS(ns,"circle");
      c.setAttribute("cx",(rnd()*300).toFixed(1)); c.setAttribute("cy",(rnd()*190).toFixed(1));
      c.setAttribute("r",(0.6+rnd()*1.6).toFixed(1)); c.setAttribute("fill","#f6e7b4"); c.setAttribute("class","twinkle");
      g.appendChild(c);
    }
    sky.insertBefore(g, sky.firstChild);
  })();

  /* 6. diya blessing */
  var wishes = ["May your home always glow with joy.","Blessings of love and light to you.","May happiness walk beside you always.","Thank you for being part of our story."];
  var wi=0, diya=$("diya");
  diya.addEventListener("click", function(){
    diya.classList.add("lit");
    $("blessing").textContent = wishes[wi++ % wishes.length];
    burst($("message"), diya, 12);
  });

  /* 7. gallery: real photos only if supplied, else ornamental artwork */
  (function(){
    var g=$("gallery"), icons=["#lotus","#flower","#lotus"];
    for(var i=0;i<3;i++){
      var d=document.createElement("div"); d.className="ph";
      if(PHOTOS[i]){ var im=new Image(); im.alt="Photograph"; im.loading="lazy"; im.src=PHOTOS[i]; d.appendChild(im); }
      else d.innerHTML='<svg viewBox="0 0 40 40" style="color:#e8cd87" aria-hidden="true"><use href="'+icons[i]+'"/></svg>';
      g.appendChild(d);
    }
    $("galleryNote").textContent = PHOTOS.length ? "" : "Photographs coming soon.";
  })();

  /* 8. calendar download (all-day event: no invented time, venue or duration) */
  function esc(t){return t.replace(/\\/g,"\\\\").replace(/;/g,"\\;").replace(/,/g,"\\,").replace(/\n/g,"\\n")}
  $("icsBtn").addEventListener("click", function(){
    var desc = "Wedding celebration of "+CFG.groom+" and "+CFG.bride+".\nReception of Bazaar - 8:00 PM\nDinner - 9:00 PM\nDoli - Taaron Ki Chhaon Mein";
    if(CFG.mapsUrl) desc += "\nLocation: "+CFG.mapsUrl;
    var now = new Date().toISOString().replace(/[-:]/g,"").split(".")[0]+"Z";
    var lines = ["BEGIN:VCALENDAR","VERSION:2.0","PRODID:-//Keshav and Anila Wedding//EN","CALSCALE:GREGORIAN","METHOD:PUBLISH",
      "BEGIN:VEVENT","UID:keshav-anila-20261205@wedding-invite","DTSTAMP:"+now,
      "DTSTART;VALUE=DATE:20261205","DTEND;VALUE=DATE:20261206",
      "SUMMARY:"+esc("Wedding of Keshav & Anila"),"DESCRIPTION:"+esc(desc),
      "BEGIN:VALARM","TRIGGER:-P1D","ACTION:DISPLAY","DESCRIPTION:Wedding tomorrow","END:VALARM",
      "END:VEVENT","END:VCALENDAR"];
    var ics = lines.join("\r\n");
    var msg = $("saveMsg");
    try{
      var blob = new Blob([ics],{type:"text/calendar;charset=utf-8"});
      var url = URL.createObjectURL(blob);
      var a = document.createElement("a"); a.href=url; a.download="Keshav-Anila-Wedding.ics";
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function(){URL.revokeObjectURL(url)},4000);
      msg.textContent = "Calendar invitation downloaded. Open it to add 5 December 2026.";
    }catch(e){
      window.open("data:text/calendar;charset=utf-8,"+encodeURIComponent(ics),"_blank");
      msg.textContent = "Open the file that appeared to add it to your calendar.";
    }
  });

  /* WhatsApp share of the deployed URL */
  function siteUrl(){
    if(CFG.siteUrl) return CFG.siteUrl;
    try{ var u = window.parent.location.href.split("#")[0]; if(u) return u; }catch(e){}
    try{ if(document.referrer) return document.referrer.split("#")[0]; }catch(e){}
    return "";
  }
  $("waBtn").addEventListener("click", function(){
    var u = siteUrl();
    if(!u || /^(about|blob|data):/.test(u)){
      $("saveMsg").textContent = "Set SITE_URL in app.py to your deployed address to enable sharing."; return;
    }
    var text = "You are warmly invited to the wedding of "+CFG.groom+" & "+CFG.bride+" on 5 December 2026. "+u;
    window.open("https://wa.me/?text="+encodeURIComponent(text),"_blank","noopener");
  });

  /* 9. maps (never invented) */
  (function(){
    var b=$("mapBtn"), n=$("locNote");
    if(CFG.mapsUrl){ b.href = CFG.mapsUrl; n.textContent = "Opens in Google Maps."; }
    else{
      b.setAttribute("aria-disabled","true"); b.removeAttribute("target"); b.href="#";
      b.addEventListener("click",function(e){e.preventDefault()});
      n.textContent = "Location details will be shared soon.";
    }
  })();

  /* 10. finale stars */
  (function(){
    var box=$("stars"), seed=3; function rnd(){ seed=(seed*9301+49297)%233280; return seed/233280; }
    for(var i=0;i<60;i++){
      var s=document.createElement("i");
      s.style.left=(rnd()*100)+"%"; s.style.top=(rnd()*100)+"%";
      s.style.animationDelay=(rnd()*3)+"s"; var z=1+rnd()*3; s.style.width=s.style.height=z+"px";
      box.appendChild(s);
    }
  })();
})();
</script>
</body>
</html>
"""

# --------------------------------------------------------------------------
# STREAMLIT SHELL
# --------------------------------------------------------------------------

st.set_page_config(
    page_title="Keshav & Anila | Wedding Invitation",
    page_icon="🪔",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit chrome so the invitation feels like a standalone website.
st.markdown(
    """
    <style>
      header[data-testid="stHeader"], footer, #MainMenu,
      div[data-testid="stToolbar"], div[data-testid="stDecoration"],
      div[data-testid="stStatusWidget"]{display:none!important}
      .stApp{background:#fbf3e4}
      .block-container{padding:0!important;max-width:100%!important}
      iframe{border:0}
    </style>
    """,
    unsafe_allow_html=True,
)

page = HTML.replace("__CONFIG__", json.dumps(CONFIG))

# The page expands its own iframe to the full browser viewport (see script),
# so the guest scrolls one continuous website, with no tiny inner scrollbar.
components.html(page, height=900, scrolling=True)
