import asyncio
from datetime import datetime
from anthropic import Anthropic
from config import *

class SimpleContentGenerator:
    def __init__(self):
        config_errors = validate_config()
        if config_errors:
            raise ValueError(f"Configuration errors: {', '.join(config_errors)}")
        
        self.client = Anthropic(api_key=ANTHROPIC_API_KEY)
        self.brand_voice = f"""
        Brand Voice for {COMPANY_PROFILE['name']}:
        POSITIONING: Leading authority in AI SaaS monitoring
        TONE: Authoritative yet approachable, technical but accessible
        TARGET AUDIENCE: {COMPANY_PROFILE['target_audience']}
        FOCUS: Practical solutions and actionable insights
        """
    
    async def _call_claude(self, prompt):
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=4000,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            raise Exception(f"Claude API error: {str(e)}")
    
    async def generate_twitter_thread(self, topic):
        prompt = f"""
        {self.brand_voice}
        
        Create a Twitter thread about: {topic}
        
        Requirements:
        - 5-6 tweets maximum
        - First tweet must be compelling hook
        - Each tweet under 280 characters
        - Include relevant AI/ML hashtags
        - End with engagement question
        - Focus on practical value for {COMPANY_PROFILE['target_audience']}
        
        Format as: 1/🧵, 2/🧵, etc.
        """
        
        try:
            content = await self._call_claude(prompt)
            return {
                'success': True,
                'content': content,
                'topic': topic,
                'type': 'twitter_thread',
                'created_at': datetime.now().isoformat()
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'topic': topic,
                'type': 'twitter_thread'
            }
    
    async def generate_linkedin_post(self, topic):
        prompt = f"""
        {self.brand_voice}
        
        Create a LinkedIn post about: {topic}
        
        Requirements:
        - Professional and engaging tone
        - Under 1300 characters
        - Strong opening line
        - Include practical insights
        - End with thought-provoking question
        - Use relevant hashtags
        - Target {COMPANY_PROFILE['target_audience']}
        """
        
        try:
            content = await self._call_claude(prompt)
            return {
                'success': True,
                'content': content,
                'topic': topic,
                'type': 'linkedin_post',
                'created_at': datetime.now().isoformat()
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'topic': topic,
                'type': 'linkedin_post'
            }
    
    async def generate_blog_post(self, topic):
        prompt = f"""
        {self.brand_voice}
        
        Write a comprehensive blog post about: {topic}
        
        Structure:
        1. Compelling headline
        2. Executive summary
        3. Problem statement and context
        4. Detailed explanation with examples
        5. Best practices and solutions
        6. Key takeaways
        7. Call-to-action
        
        Requirements:
        - 1200-1800 words
        - Technical but accessible
        - Include practical examples
        - Provide actionable insights
        """
        
        try:
            content = await self._call_claude(prompt)
            return {
                'success': True,
                'content': content,
                'topic': topic,
                'type': 'blog_post',
                'created_at': datetime.now().isoformat()
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'topic': topic,
                'type': 'blog_post'
            }

async def test_generator():
    print("🧪 Testing Content Generator...")
    try:
        generator = SimpleContentGenerator()
        result = await generator.generate_twitter_thread("AI Model Drift Detection")
        if result['success']:
            print("✅ Content generation working!")
            print(f"Preview: {result['content'][:200]}...")
        else:
            print(f"❌ Error: {result['error']}")
    except Exception as e:
        print(f"❌ Setup Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_generator())
