



// "use client";

// import { useState, useEffect } from "react";

// export default function Home() {
//   const [text, setText] = useState("");
//   const [voices, setVoices] = useState<SpeechSynthesisVoice[]>([]);
//   const [voice, setVoice] = useState<string>("");
//   const [loading, setLoading] = useState(false);

//   useEffect(() => {
//     const synth = window.speechSynthesis;

//     const loadVoices = () => {
//       const availableVoices = synth.getVoices();
//       if (availableVoices.length > 0) {
//         setVoices(availableVoices);
//         setVoice(availableVoices[0].name);
//       }
//     };

//     // Load voices initially
//     loadVoices();

//     // Add event listener for voice changes (especially on mobile)
//     synth.onvoiceschanged = loadVoices;

//     return () => {
//       synth.onvoiceschanged = null; // Cleanup
//     };
//   }, []);

//   const handleConvert = () => {
//     if (!text) return alert("Please enter text");
//     if (!voices.length) return alert("No voices available. Try again later.");

//     setLoading(true);
//     const synth = window.speechSynthesis;
//     const utterance = new SpeechSynthesisUtterance(text);
//     const selectedVoice = voices.find((v) => v.name === voice);

//     if (selectedVoice) utterance.voice = selectedVoice;

//     synth.speak(utterance);
//     utterance.onend = () => setLoading(false);
//   };

//   const handleDownload = () => {
//     if (!text) return alert("Please enter text");

//     const blob = new Blob([text], { type: "text/plain" });
//     const url = URL.createObjectURL(blob);
//     const a = document.createElement("a");
//     a.href = url;
//     a.download = "speech.txt";
//     document.body.appendChild(a);
//     a.click();
//     document.body.removeChild(a);
//   };

//   return (
//     <div className="min-h-screen flex flex-col items-center justify-center p-4 bg-gray-100">
//       <h1 className="text-2xl font-bold mb-4">AI Text to Speech</h1>
//       <textarea
//         className="w-full max-w-lg p-2 border rounded-lg"
//         rows={4}
//         placeholder="Enter text here..."
//         value={text}
//         onChange={(e) => setText(e.target.value)}
//       />
//       <select
//         className="w-full max-w-lg p-2 border rounded-lg my-3"
//         value={voice}
//         onChange={(e) => setVoice(e.target.value)}
//       >
//         {voices.map((v) => (
//           <option key={v.name} value={v.name}>
//             {v.name}
//           </option>
//         ))}
//       </select>
//       <div className="flex gap-4">
//         <button
//           className="bg-blue-500 text-white px-4 py-2 rounded-lg"
//           onClick={handleConvert}
//           disabled={loading}
//         >
//           {loading ? "Converting..." : "Play"}
//         </button>
//         <button
//           className="bg-green-500 text-white px-4 py-2 rounded-lg"
//           onClick={handleDownload}
//           disabled={loading}
//         >
//           {loading ? "Downloading..." : "Download"}
//         </button>
//       </div>
//     </div>
//   );
// }









"use client";

import { useState, useEffect } from "react";

export default function Home() {
  const [text, setText] = useState("");
  const [voices, setVoices] = useState<SpeechSynthesisVoice[]>([]);
  const [voice, setVoice] = useState<string>("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const synth = window.speechSynthesis;

    const loadVoices = () => {
      const availableVoices = synth.getVoices();
      if (availableVoices.length > 0) {
        setVoices(availableVoices);
        setVoice((prev) =>
          availableVoices.some((v) => v.name === prev) ? prev : availableVoices[0].name
        );
      }
    };

    // Load voices with a delay to ensure they are populated
    const interval = setInterval(() => {
      if (synth.getVoices().length > 0) {
        loadVoices();
        clearInterval(interval);
      }
    }, 200);

    synth.onvoiceschanged = loadVoices;

    return () => {
      synth.onvoiceschanged = null;
      clearInterval(interval);
    };
  }, []);

  const handleConvert = () => {
    if (!text) return alert("Please enter text");
    if (!voices.length) return alert("No voices available. Try again later.");

    setLoading(true);
    const synth = window.speechSynthesis;
    const utterance = new SpeechSynthesisUtterance(text);
    const selectedVoice = voices.find((v) => v.name === voice);

    if (selectedVoice) utterance.voice = selectedVoice;

    synth.speak(utterance);
    utterance.onend = () => setLoading(false);
  };

  const handleDownload = () => {
    if (!text) return alert("Please enter text");

    const blob = new Blob([text], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "speech.txt";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-4 bg-gray-100">
      <h1 className="text-2xl font-bold mb-4">AI Text to Speech</h1>
      <textarea
        className="w-full max-w-lg p-2 border rounded-lg"
        rows={4}
        placeholder="Enter text here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <select
        className="w-full max-w-lg p-2 border rounded-lg my-3"
        value={voice}
        onChange={(e) => setVoice(e.target.value)}
      >
        {voices.map((v) => (
          <option key={v.name} value={v.name}>
            {v.name}
          </option>
        ))}
      </select>
      <div className="flex gap-4">
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded-lg"
          onClick={handleConvert}
          disabled={loading}
        >
          {loading ? "Converting..." : "Play"}
        </button>
        <button
          className="bg-green-500 text-white px-4 py-2 rounded-lg"
          onClick={handleDownload}
          disabled={loading}
        >
          {loading ? "Downloading..." : "Download"}
        </button>
      </div>
    </div>
  );
}
