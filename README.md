<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UDUS NEWSLINE</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #1e3d24;
            color: #fff;
        }

        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            background-color: #2a5934;
        }

        .navbar a {
            color: #fff;
            text-decoration: none;
            padding: 10px 15px;
        }

        .navbar a:hover {
            background-color: #3a7043;
            border-radius: 5px;
        }

        .search-bar {
            margin: 20px auto;
            display: flex;
            justify-content: center;
        }

        .search-bar input {
            padding: 10px;
            width: 50%;
            border-radius: 5px 0 0 5px;
            border: none;
        }

        .search-bar button {
            padding: 10px;
            background-color: #4caf50;
            color: white;
            border: none;
            border-radius: 0 5px 5px 0;
            cursor: pointer;
        }

        .search-bar button:hover {
            background-color: #45a049;
        }

        .news-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            padding: 20px;
        }

        .news-item {
            background-color: #2a5934;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        }

        .news-item img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }

        .news-content {
            padding: 15px;
        }

        .news-content h3 {
            margin: 0;
            font-size: 18px;
            color: #ffc107;
        }

        .news-content p {
            margin: 10px 0 0;
        }

        .news-content a {
            display: inline-block;
            margin-top: 10px;
            color: #ff9800;
            text-decoration: none;
        }

        .news-content a:hover {
            text-decoration: underline;
        }
    </style>
</head>

<body>
    <nav class="navbar">
        <h1>UDUS NEWSLINE</h1>
        <div>
            <a href="#">Home</a>
            <a href="#">About</a>
            <a href="#">News/Post</a>
        </div>
    </nav>

    <div class="search-bar">
        <input type="text" id="searchInput" placeholder="Search news...">
        <button onclick="searchNews()">Search</button>
    </div>

    <div id="newsContainer" class="news-container">
        <div class="news-item">
            <div class="news-content">
                <h3>UDUS Holds 2024 Convocation Ceremony</h3>
                <p>The University’s 2024 Convocation Ceremony was a grand success, with numerous distinguished guests, faculty, and students celebrating academic achievements. The ceremony featured speeches from the Chancellor and Vice Chancellor, celebrating the accomplishments of the graduating students.</p>
                <a href="convocation.html">Read more</a>
            </div>
        </div>

        <div class="news-item">
            <div class="news-content">
                <h3>New Hostels Commissioned</h3>
                <p>Usmanu Danfodiyo University has just commissioned a new set of hostels aimed at improving accommodation for students. The Vice Chancellor emphasized the university’s commitment to providing a conducive living environment for student growth.</p>
                <a href="hostel.html">Read more</a>
            </div>
        </div>

        <div class="news-item">
            <div class="news-content">
                <h3>Latest Academic Calendar Updates</h3>
                <p>The university has recently updated its academic calendar with new dates for resumption, exams, and holidays. Students are advised to review the calendar to ensure they do not miss key academic events.</p>
                <a href="calendar.html">Read more</a>
            </div>
        </div>

        <div class="news-item">
            <div class="news-content">
                <h3>Student Achievements and Success Stories</h3>
                <p>UDUS celebrates the achievements of its students in academics, sports, and extracurricular activities. These success stories serve as an inspiration to their peers and demonstrate the potential for growth within the university community.</p>
                <a href="academic.html">Read more</a>
            </div>
        </div>

        <div class="news-item">
            <div class="news-content">
                <h3>Upcoming Events and Activities</h3>
                <p>UDUS announces upcoming events such as the annual matriculation ceremony, career fairs, workshops, and cultural festivals. Students are encouraged to participate to enhance their academic and social experiences.</p>
                <a href="events.html">Read more</a>
            </div>
        </div>

        <div class="news-item">
            <div class="news-content">
                <h3>Campus News and Developments</h3>
                <p>Significant developments are taking place on campus, including infrastructure upgrades and improvements to campus safety. These changes are aimed at creating a better environment for students and faculty.</p>
                <a href="news.html">Read more</a>
            </div>
        </div>

        <div class="news-item">
            <div class="news-content">
                <h3>Tips for Academic Success</h3>
                <p>UDUS has compiled a series of tips and resources to help students succeed academically, including effective study techniques, time management strategies, and advice on balancing academic work with extracurricular activities.</p>
                <a href="academic.html">Read more</a>
            </div>
        </div>

        <div class="news-item">
            <div class="news-content">
                <h3>Profiles of Faculty and Alumni</h3>
                <p>UDUS highlights inspiring faculty members and successful alumni. These profiles serve as motivation for current students, demonstrating the various paths to success after graduation.</p>
                <a href="news.html">Read more</a>
            </div>
        </div>

        <div class="news-item">
            <div class="news-content">
                <h3>Health, Safety, and Wellness Tips</h3>
                <p>UDUS is committed to ensuring the health and safety of its students by offering wellness programs focused on mental health, stress management, and maintaining a healthy lifestyle. Students are encouraged to participate.</p>
                <a href="health.html">Read more</a>
            </div>
        </div>

        <div class="news-item">
            <div class="news-content">
                <h3>UDUS Admission 2024/2025 Academic Session: Confirmation of Admission Ongoing</h3>
                <p>The confirmation of admission for the 2024/2025 academic session is currently ongoing. All candidates who participated in the admission process are encouraged to confirm their admission status to proceed with registration.</p>
                <a href="admission.html">Read more</a>
            </div>
        </div>

    </div>
     <script>
        const newsArticles = [
            {
                title: "UDUS Holds 2024 Convocation Ceremony",
                content: "The University’s 2024 Convocation Ceremony was a grand success...",
                image: "file:///C:/Users/BEN%20CONCEPT/Desktop/UDUS%20NEWSLINE/convocation.jpg",
                link: "file:///C:/Users/BEN%20CONCEPT/Desktop/UDUS%20NEWSLINE/convocation.html"
            },
            {
                title: "New Hostels Commissioned",
                content: "Usmanu Danfodiyo University has just commissioned a new set of hostels...",
                image: "file:///C:/Users/BEN%20CONCEPT/Desktop/UDUS%20NEWSLINE/hostel.jpg",
                link: "file:///C:/Users/BEN%20CONCEPT/Desktop/UDUS%20NEWSLINE/hostel.html"
            },
            {
                title: "Latest Academic Calendar Updates",
                content: "The university has recently updated its academic calendar...",
                image: "file:///C:/Users/BEN%20CONCEPT/Desktop/UDUS%20NEWSLINE/calendar.jpg",
                link: "file:///C:/Users/BEN%20CONCEPT/Desktop/UDUS%20NEWSLINE/calendar.html"
            },
            {
                title: "Student Achievements and Success Stories",
                content: "Usmanu Danfodiyo University is proud to highlight the achievements of its students...",
                image: "file:///C:/Users/BEN%20CONCEPT/Desktop/UDUS%20NEWSLINE/alumni.jpg",
                link: "file:///C:/Users/BEN%20CONCEPT/Desktop/UDUS%20NEWSLINE/academic.html"
            },
            {
                title: "Upcoming Events and Activities",
                content: "UDUS is excited to announce a number of upcoming events...",
                image: "file:///C:/Users/BEN%20CONCEPT/Desktop/UDUS%20NEWSLINE/event.jpg",
                link: "file:///C:/Users/BEN%20CONCEPT/Desktop/UDUS%20NEWSLINE/events.html"
            },
            {
                title: "Campus News and Developments",
                content: "Significant developments are taking place on campus...",
                image: "file:///C:/Users/BEN%20CONCEPT/Desktop/UDUS%20NEWSLINE/news.jpg",
                link: "file:///C:/Users/BEN%20CONCEPT/Desktop/UDUS%20NEWSLINE/news.html"
            },
            {
                title: "Tips for Academic Success",
                content: "To help students succeed academically, the university has compiled a series of tips...",
                image: "file:///C:/Users/BEN%20CONCEPT/Desktop/UDUS%20NEWSLINE/tips.jpg",
                link: "file:///C:/Users/BEN%20CONCEPT/Desktop/UDUS%20NEWSLINE/tips.html"
            },
            {
                title: "Profiles of Faculty and Alumni",
                content: "UDUS takes pride in its exceptional faculty and successful alumni...",
                image: "file:///C:/Users/BEN%20CONCEPT/Desktop/UDUS%20NEWSLINE/alumni.jpg",
                link: "file:///C:/Users/BEN%20CONCEPT/Desktop/UDUS%20NEWSLINE/alumni.html"
            },
            {
                title: "Health, Safety, and Wellness Tips",
                content: "The university is committed to ensuring the health and safety of its students...",
                image: "file:///C:/Users/BEN%20CONCEPT/Desktop/UDUS%20NEWSLINE/health.jpg",
                link: "file:///C:/Users/BEN%20CONCEPT/Desktop/UDUS%20NEWSLINE/health.html"
            }
            
        ];

               function displayNews(articles) {
            const newsContainer = document.getElementById("newsContainer");
            newsContainer.innerHTML = ""; // Clear the container before adding new articles

            articles.forEach(article => {
                const newsItem = document.createElement("div");
                newsItem.className = "news-item";

                newsItem.innerHTML = `
                    <img src="${article.image}" alt="${article.title}">
                    <div class="news-content">
                        <h3>${article.title}</h3>
                        <p>${article.content}</p>
                        <a href="${article.link}" target="_blank">Read more</a>
                    </div>
                `;

                newsContainer.appendChild(newsItem);
            });
        }

        function searchNews() {
            const searchInput = document.getElementById("searchInput").value.toLowerCase();
            const filteredArticles = newsArticles.filter(article =>
                article.title.toLowerCase().includes(searchInput) ||
                article.content.toLowerCase().includes(searchInput)
            );

            if (filteredArticles.length > 0) {
                displayNews(filteredArticles);
            } else {
                const newsContainer = document.getElementById("newsContainer");
                newsContainer.innerHTML = `<p style="text-align:center;">No articles found matching your search.</p>`;
            }
        }

        // Display all news articles on page load
        displayNews(newsArticles);

    </script>

</body>

</html>
