import { useViewer } from './engine/useViewer';
import { Compatibility } from './engine/Compatibility';
import { ChannelPanel, Library, Screen } from './engine/Viewer';
import './base.css';
import './styles.css';

function Archive() {
  const viewer = useViewer('democracy_now_vid');
  return <main>
    <a className="skip-link" href="#library">Skip to broadcast archive</a>
    <header className="masthead"><a className="brand" href="/" aria-label="Democracy Now! archive home"><img src="/assets/democracy-now.svg" alt="Democracy Now!" /></a><div className="edition"><p>THE WAR AND PEACE REPORT</p><span>Broadcast archive</span></div><nav aria-label="Main navigation"><a href="#screen">Watch the replay</a><a href="#library">Browse broadcasts</a></nav></header>
    <div className="archive-bar"><span>INDEPENDENT NEWS. A PUBLIC RECORD.</span><span>ON DEMAND / SCHEDULED REPLAY</span></div>
    <section className="screen-layout" aria-label="Broadcast viewing"><Screen viewer={viewer}><div className="news-intro"><div className="photo"><img src="/assets/amy-goodman.png" alt="Amy Goodman reporting with a Democracy Now! microphone" /><span>DEMOCRACY NOW! / FROM THE ARCHIVE</span></div><p className="eyebrow">THE BROADCAST RECORD</p><h1>Return to the report.</h1><p className="lede">Watch a broadcast from the beginning, or join the replay already on the channel. The original date stays with every program.</p></div></Screen><ChannelPanel viewer={viewer} /></section>
    <Library viewer={viewer} heading="Broadcast archive" mark="DN!" />
    <footer><strong>Democracy Now! broadcast archive</strong><span>Independent archive viewer · Video streamed from Internet Archive<br />Original reporting, dates, and source attribution retained.</span><a href="https://www.democracynow.org/" target="_blank" rel="noreferrer">Visit Democracy Now! ↗</a></footer>
  </main>;
}
export default function App() { return <Compatibility collection="democracy_now_vid"><Archive /></Compatibility>; }
