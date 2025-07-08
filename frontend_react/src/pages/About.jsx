
const About = () => {
  return (
    <section className="py-20 px-6">
      <div className="max-w-5xl mx-auto space-y-16">
        {/* Project Overview */}
        <div className="bg-white p-8 rounded-lg shadow-md">
          <h2 className="text-3xl font-bold text-gray-800 mb-4">About the Project</h2>
          <p className="text-gray-700 text-lg leading-relaxed">
            This project uses Premier League match data from the 2020 to the 2025 seasons to predict match outcomes.
            All datasets are free and open source from{' '}
            <a
              href="https://www.football-data.co.uk/englandm.php"
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-600 underline hover:text-blue-800"
            >
              football-data.co.uk
            </a>
            . The data is cleansed and passed through logistic regression and random forest classifiers to generate accurate predictions.
            The application is built with a Django REST backend and a modern React frontend.
          </p>
        </div>

        {/* About You */}
        <div className="bg-white p-8 rounded-lg shadow-md flex flex-col md:flex-row items-start gap-6">
          {/* Optional profile image */}
          {/* <img src="/profile.jpg" alt="Christian Rodriguez" className="w-32 h-32 rounded-full object-cover shadow" /> */}
          <img
            src="/bellingham.jpg"
            alt="Christian with Jude Bellingham"
            className="w-64 h-64 rounded-full object-cover border-4 border-white shadow-md"
          />

          <div>
            <h2 className="text-3xl font-bold text-gray-800 mb-4">About Me</h2>
            <p className="text-gray-700 text-lg leading-relaxed mb-4">
              I'm Christian Rodriguez, a Software Engineer at NASA with a passion for soccer and data science. This project is a blend of both and 
              a way to showcase my technical skills while building a tool that's fun and useful.
              I love watching and playing soccer, and enjoy using data to solve real-world problems.
            </p>

            <a
              href="https://www.linkedin.com/in/christian-rodriguezucf/"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center text-blue-600 hover:text-blue-800 font-semibold"
            >
              {/* <FaLinkedin className="mr-2" /> */}
              Connect on LinkedIn
            </a>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;