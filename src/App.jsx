import { useState, useMemo, useEffect } from 'react'
import Fuse from 'fuse.js'
import SearchBar from './components/SearchBar'
import ServiceCard from './components/ServiceCard'

function App() {
  const [searchQuery, setSearchQuery] = useState('')
  const [selectedDepartment, setSelectedDepartment] = useState('all')
  const [showDropdown, setShowDropdown] = useState(false)
  const [servicesData, setServicesData] = useState({ metadata: {}, services: [] })
  const [loading, setLoading] = useState(true)

  // Fetch services data
  useEffect(() => {
    fetch('/services.json')
      .then(res => res.json())
      .then(data => {
        setServicesData(data)
        setLoading(false)
      })
      .catch(err => {
        console.error('Error loading services:', err)
        setLoading(false)
      })
  }, [])

  // Fuzzy search configuration
  const fuse = useMemo(() => {
    if (!servicesData.services || servicesData.services.length === 0) {
      return null
    }
    return new Fuse(servicesData.services, {
      keys: ['name.en', 'name.te', 'keywords', 'department'],
      threshold: 0.3,
      includeScore: true
    })
  }, [servicesData.services])

  // Filter services
  const filteredServices = useMemo(() => {
    if (!servicesData.services || servicesData.services.length === 0) {
      return []
    }

    let results = servicesData.services

    // Apply fuzzy search if query exists
    if (searchQuery.trim() && fuse) {
      const fuseResults = fuse.search(searchQuery)
      results = fuseResults.map(result => result.item)
    }

    // Apply department filter
    if (selectedDepartment !== 'all') {
      results = results.filter(s => s.department === selectedDepartment)
    }

    // Sort by priority
    return results.sort((a, b) => a.priority_rank - b.priority_rank)
  }, [searchQuery, selectedDepartment, fuse, servicesData.services])

  // Get unique departments
  const departments = useMemo(() => {
    if (!servicesData.services || servicesData.services.length === 0) {
      return []
    }
    const depts = [...new Set(servicesData.services.map(s => s.department))]
    return depts.sort()
  }, [servicesData.services])

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-orange-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-16 w-16 border-b-2 border-telangana-primary mx-auto mb-4"></div>
          <p className="text-gray-600 text-lg">Loading MeeMarg...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-orange-50">
      {/* Header */}
      <header className="bg-telangana-secondary text-white shadow-lg">
        <div className="container mx-auto px-4 py-6">
          <h1 className="text-3xl font-bold">MeeMarg</h1>
          <p className="text-blue-100 mt-1">మీమార్గ్ - Telangana Government Services Navigator</p>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 py-8">
        {/* Search Section */}
        <div className="max-w-4xl mx-auto mb-8">
          <SearchBar
            searchQuery={searchQuery}
            setSearchQuery={setSearchQuery}
            showDropdown={showDropdown}
            setShowDropdown={setShowDropdown}
            departments={departments}
            selectedDepartment={selectedDepartment}
            setSelectedDepartment={setSelectedDepartment}
          />
        </div>

        {/* Stats */}
        <div className="max-w-4xl mx-auto mb-6">
          <div className="bg-white rounded-lg shadow p-4 flex justify-between items-center">
            <div>
              <p className="text-gray-600">Showing <span className="font-bold text-telangana-primary">{filteredServices.length}</span> of {servicesData.services.length} services</p>
            </div>
            <div className="text-sm text-gray-500">
              Today: {new Date().toLocaleDateString('en-IN', {
                day: 'numeric',
                month: 'numeric',
                year: 'numeric',
                timeZone: 'Asia/Kolkata'
              })}
            </div>
          </div>
        </div>

        {/* Services Grid */}
        <div className="max-w-4xl mx-auto grid gap-6">
          {filteredServices.length > 0 ? (
            filteredServices.map(service => (
              <ServiceCard key={service.service_id} service={service} />
            ))
          ) : (
            <div className="text-center py-12">
              <p className="text-gray-500 text-lg">No services found matching your search.</p>
              <p className="text-gray-400 mt-2">Try different keywords or clear filters.</p>
            </div>
          )}
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-gray-800 text-white mt-16 py-6">
        <div className="container mx-auto px-4 text-center">
          <p>© {new Date().getFullYear()} MeeMarg - Telangana Government Services</p>
          <p className="text-gray-400 text-sm mt-2">Built with ❤️ for Citizens of Telangana</p>
        </div>
      </footer>
    </div>
  )
}

export default App

// Made with Bob
