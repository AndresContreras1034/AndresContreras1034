#!/usr/bin/env python3
"""
Main script for GitHub profile automation and data analysis
Author: Andrés Méndez (AndresContreras1034)
Description: Automation script for profile maintenance and data processing
"""

import json
import datetime
import os
import sys
from typing import Dict, List, Any


class ProfileManager:
    """Manages GitHub profile data and automation tasks"""
    
    def __init__(self):
        self.profile_data = {
            "name": "Andrés Méndez",
            "role": "Systems Engineering Student",
            "semester": "6th",
            "age": 19,
            "focus_areas": ["Backend", "Automation", "Data Analysis"],
            "last_updated": None
        }
        
    def update_timestamp(self) -> None:
        """Update the last updated timestamp"""
        self.profile_data["last_updated"] = datetime.datetime.now().isoformat()
        
    def get_current_stack(self) -> Dict[str, List[str]]:
        """Get the current technology stack (2025)"""
        return {
            "backend": ["Java", "Python", "Spring Boot", "SQL"],
            "frontend": ["HTML/CSS", "JavaScript (basic)"],
            "devtools": ["Git", "VSCode", "Power BI", "VirtualBox"],
            "os": ["Linux (Kali/Ubuntu)", "Windows"],
            "databases": ["MySQL", "SQLite", "MongoDB"]
        }
        
    def calculate_experience_years(self) -> float:
        """Calculate years of programming experience"""
        # Assuming started programming in 2022 based on student status
        start_date = datetime.date(2022, 1, 1)
        current_date = datetime.date.today()
        experience_days = (current_date - start_date).days
        return round(experience_days / 365.25, 1)
        
    def generate_profile_stats(self) -> Dict[str, Any]:
        """Generate profile statistics"""
        return {
            "experience_years": self.calculate_experience_years(),
            "technologies_count": len(self.get_current_stack()["backend"]) + 
                                 len(self.get_current_stack()["frontend"]),
            "focus_areas": len(self.profile_data["focus_areas"]),
            "semester_progress": f"{self.profile_data['semester']} semester",
            "age": self.profile_data["age"]
        }
        
    def display_profile_info(self) -> None:
        """Display current profile information"""
        print("=" * 50)
        print(f"GitHub Profile: {self.profile_data['name']}")
        print("=" * 50)
        print(f"Role: {self.profile_data['role']}")
        print(f"Current Semester: {self.profile_data['semester']}")
        print(f"Age: {self.profile_data['age']} years old")
        print(f"Focus Areas: {', '.join(self.profile_data['focus_areas'])}")
        
        stats = self.generate_profile_stats()
        print(f"\nExperience: {stats['experience_years']} years")
        print(f"Technologies: {stats['technologies_count']}+ tools/languages")
        
        stack = self.get_current_stack()
        print(f"\nCurrent Stack (2025):")
        for category, technologies in stack.items():
            print(f"  {category.title()}: {', '.join(technologies)}")
            
        if self.profile_data["last_updated"]:
            print(f"\nLast Updated: {self.profile_data['last_updated']}")
        print("=" * 50)


class DataAnalyzer:
    """Simple data analysis utilities"""
    
    @staticmethod
    def analyze_project_status(projects: List[Dict[str, str]]) -> Dict[str, int]:
        """Analyze project status distribution"""
        status_count = {}
        for project in projects:
            status = project.get("status", "Unknown")
            status_count[status] = status_count.get(status, 0) + 1
        return status_count
        
    @staticmethod
    def get_sample_projects() -> List[Dict[str, str]]:
        """Get sample project data based on README"""
        return [
            {"name": "Cheap Flight Tracker", "status": "Completed", "tech": "Python"},
            {"name": "COVID-19 Dashboard", "status": "In Progress", "tech": "Power BI"},
            {"name": "Secure Password Generator", "status": "Prototype", "tech": "Java"},
            {"name": "Pet Tracker", "status": "In Development", "tech": "Java"},
            {"name": "Portfolio Analyzer", "status": "Planned", "tech": "Python"},
            {"name": "Smart Reminder App", "status": "Planned", "tech": "React Native"}
        ]


def main():
    """Main function to demonstrate profile automation"""
    print("🚀 GitHub Profile Automation Script")
    print("Author: Andrés Méndez (AndresContreras1034)")
    print()
    
    # Initialize profile manager
    profile_manager = ProfileManager()
    profile_manager.update_timestamp()
    
    # Display profile information
    profile_manager.display_profile_info()
    
    # Analyze projects
    print("\n📊 Project Analysis:")
    data_analyzer = DataAnalyzer()
    projects = data_analyzer.get_sample_projects()
    status_analysis = data_analyzer.analyze_project_status(projects)
    
    print("Project Status Distribution:")
    for status, count in status_analysis.items():
        print(f"  {status}: {count} project(s)")
        
    # Technology distribution
    tech_count = {}
    for project in projects:
        tech = project.get("tech", "Unknown")
        tech_count[tech] = tech_count.get(tech, 0) + 1
        
    print("\nTechnology Usage in Projects:")
    for tech, count in sorted(tech_count.items(), key=lambda x: x[1], reverse=True):
        print(f"  {tech}: {count} project(s)")
    
    # Save profile data
    output_file = "profile_data.json"
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                "profile": profile_manager.profile_data,
                "stats": profile_manager.generate_profile_stats(),
                "projects": projects,
                "analysis": {
                    "status_distribution": status_analysis,
                    "technology_distribution": tech_count
                }
            }, f, indent=2, ensure_ascii=False)
        print(f"\n✅ Profile data saved to {output_file}")
    except Exception as e:
        print(f"\n❌ Error saving profile data: {e}")
    
    print("\n🎯 Automation script completed successfully!")


if __name__ == "__main__":
    main()