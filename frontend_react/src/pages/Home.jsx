const Home = () => {
  return (
    <div className="relative h-screen w-full overflow-hidden">
      {/* 🔹 Fullscreen Background Video */}
      <video
        autoPlay
        muted
        loop
        className="absolute top-0 left-0 w-full h-full object-cover z-0"
      >
        <source src="/background.mp4" type="video/mp4" />
        Your browser does not support the video tag.
      </video>

      {/* 🔹 Optional dark overlay */}
      <div className="absolute top-0 left-0 w-full h-full bg-black bg-opacity-50 z-10"></div>

      {/* 🔹 Foreground Content */}
      <div className="relative z-20 flex flex-col items-center justify-center h-full text-white text-center px-4">
        <h1 className="text-5xl font-bold mb-4">Welcome to Predictor FC</h1>
        <p className="text-lg mb-6">Your go-to app for Premier League predictions.</p>
        <a
          href="/predict"
          className="px-6 py-3 bg-blue-600 text-white rounded hover:bg-blue-700 transition"
        >
          Go to Prediction
        </a>
      </div>
    </div>
  );
};


export default Home;