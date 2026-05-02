import { Search, ChevronDown } from 'lucide-react'

export default function SearchBar({ 
  searchQuery, 
  setSearchQuery, 
  showDropdown, 
  setShowDropdown,
  departments,
  selectedDepartment,
  setSelectedDepartment 
}) {
  return (
    <div className="relative">
      <div className="flex gap-2">
        {/* Search Input */}
        <div className="flex-1 relative">
          <Search className="absolute left-4 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            onFocus={() => !searchQuery && setShowDropdown(true)}
            placeholder="Search services... (e.g., 'birth certificate', 'ration card')"
            className="w-full pl-12 pr-4 py-4 text-lg border-2 border-gray-300 rounded-lg focus:border-telangana-primary focus:outline-none transition-colors"
          />
        </div>

        {/* Department Filter */}
        <select
          value={selectedDepartment}
          onChange={(e) => setSelectedDepartment(e.target.value)}
          className="px-6 py-4 border-2 border-gray-300 rounded-lg focus:border-telangana-primary focus:outline-none bg-white cursor-pointer"
        >
          <option value="all">All Departments</option>
          {departments.map(dept => (
            <option key={dept} value={dept}>{dept}</option>
          ))}
        </select>
      </div>

      {/* Dropdown for empty search */}
      {showDropdown && !searchQuery && (
        <div className="absolute z-10 w-full mt-2 bg-white rounded-lg shadow-xl border border-gray-200 max-h-96 overflow-y-auto">
          <div className="p-4 border-b border-gray-200 bg-gray-50">
            <h3 className="font-semibold text-gray-700">Browse by Department</h3>
          </div>
          {departments.map(dept => (
            <button
              key={dept}
              onClick={() => {
                setSelectedDepartment(dept)
                setShowDropdown(false)
              }}
              className="w-full text-left px-4 py-3 hover:bg-blue-50 transition-colors border-b border-gray-100 last:border-b-0"
            >
              <span className="font-medium text-gray-800">{dept}</span>
            </button>
          ))}
          <button
            onClick={() => setShowDropdown(false)}
            className="w-full text-center px-4 py-3 text-gray-500 hover:bg-gray-50 text-sm"
          >
            Close
          </button>
        </div>
      )}
    </div>
  )
}

// Made with Bob
