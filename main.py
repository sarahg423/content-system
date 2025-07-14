import asyncio
import os
from pathlib import Path
from datetime import datetime
from content_generator import SimpleContentGenerator
from config import COMPANY_PROFILE, AI_MONITORING_TOPICS

class AIContentSystem:
    def __init__(self):
        self.generator = SimpleContentGenerator()
        self.output_dir = Path("content_output")
        self.output_dir.mkdir(exist_ok=True)
    
    def show_banner(self):
        print("\n" + "="*60)
        print("    🤖 AI CONTENT CREATION SYSTEM")
        print(f"    Company: {COMPANY_PROFILE['name']}")
        print("="*60)
    
    def show_menu(self):
        print("\n📋 MAIN MENU")
        print("1. 📱 Generate Twitter Thread")
        print("2. 💼 Generate LinkedIn Post") 
        print("3. 📄 Generate Blog Post")
        print("4. 💡 Get Content Ideas")
        print("5. 📁 View Saved Content")
        print("6. 🚪 Exit")
    
    def save_content(self, result):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        topic_clean = result['topic'].replace(' ', '_').lower()[:30]
        filename = f"{result['type']}_{topic_clean}_{timestamp}.txt"
        filepath = self.output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"Topic: {result['topic']}\n")
            f.write(f"Type: {result['type']}\n")
            f.write(f"Generated: {result['created_at']}\n")
            f.write("="*50 + "\n\n")
            f.write(result['content'])
        
        print(f"\n💾 Content saved to: {filepath}")
    
    def view_saved_content(self):
        content_files = list(self.output_dir.glob("*.txt"))
        if not content_files:
            print("\n📁 No saved content found.")
            return
        
        print(f"\n📁 Found {len(content_files)} saved files:")
        for i, file in enumerate(content_files[-10:], 1):
            print(f"{i:2d}. {file.stem.replace('_', ' ').title()}")
    
    async def run(self):
        self.show_banner()
        
        while True:
            self.show_menu()
            choice = input("\nSelect option (1-6): ").strip()
            
            try:
                if choice == '1':
                    topic = input("\nEnter Twitter thread topic: ").strip()
                    if topic:
                        print(f"\n⏳ Generating Twitter thread: {topic}")
                        result = await self.generator.generate_twitter_thread(topic)
                        if result['success']:
                            print("\n✅ Twitter Thread Generated:")
                            print("="*60)
                            print(result['content'])
                            print("="*60)
                            self.save_content(result)
                        else:
                            print(f"❌ Error: {result['error']}")
                
                elif choice == '2':
                    topic = input("\nEnter LinkedIn post topic: ").strip()
                    if topic:
                        print(f"\n⏳ Generating LinkedIn post: {topic}")
                        result = await self.generator.generate_linkedin_post(topic)
                        if result['success']:
                            print("\n✅ LinkedIn Post Generated:")
                            print("="*60)
                            print(result['content'])
                            print("="*60)
                            self.save_content(result)
                        else:
                            print(f"❌ Error: {result['error']}")
                
                elif choice == '3':
                    topic = input("\nEnter blog post topic: ").strip()
                    if topic:
                        print(f"\n⏳ Generating blog post: {topic}")
                        result = await self.generator.generate_blog_post(topic)
                        if result['success']:
                            print("\n✅ Blog Post Generated:")
                            print("="*60)
                            preview = result['content'][:1000] + "..." if len(result['content']) > 1000 else result['content']
                            print(preview)
                            print("="*60)
                            self.save_content(result)
                        else:
                            print(f"❌ Error: {result['error']}")
                
                elif choice == '4':
                    print("\n💡 AI Monitoring Content Topics:")
                    for i, topic in enumerate(AI_MONITORING_TOPICS, 1):
                        print(f"{i:2d}. {topic}")
                
                elif choice == '5':
                    self.view_saved_content()
                
                elif choice == '6':
                    print("\n👋 Thanks for using AI Content System!")
                    break
                
                else:
                    print("❌ Invalid option. Please try again.")
            
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")

async def main():
    try:
        app = AIContentSystem()
        await app.run()
    except Exception as e:
        print(f"\n❌ Error starting application: {e}")
        print("\nPlease check:")
        print("1. Your .env file has ANTHROPIC_API_KEY set")
        print("2. You've installed all dependencies")

if __name__ == "__main__":
    asyncio.run(main())
