
from Agent1.agent1 import run_agent1
from Agent2.matching import get_score


from Agent2.update_sheet import update_sheet

if __name__ == "__main__":
    pdf_path = "Genai.pdf"
    jd = """We are looking for a skilled Java Developer to design, develop, and maintain high-performance applications. The ideal candidate should have strong experience with Java, Spring Boot, Hibernate, and RESTful APIs. You will be responsible for writing clean, scalable code and ensuring application performance and security. Experience with microservices architecture, Docker, and Kubernetes is highly desirable. The candidate should be proficient in working with SQL and NoSQL databases like MySQL, PostgreSQL, and MongoDB. Familiarity with JUnit and other testing frameworks, along with experience in CI/CD pipelines using Jenkins or GitLab, is a plus. Strong understanding of OOP principles, design patterns, and multithreading is required. The candidate will work closely with cross-functional teams to define and implement new features, resolve bugs, and ensure smooth production deployment. Experience with AWS, GCP, or Azure for cloud-based development and deployment will be an added advantage."""
    data  = run_agent1(pdf_path)
    print(data)
    score = get_score(data, jd)
    print(score)
    update_sheet(data, score)