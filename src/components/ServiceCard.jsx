import { Clock, FileText, IndianRupee, AlertCircle, Globe, Building2 } from 'lucide-react'

export default function ServiceCard({ service }) {
  const getCategoryBadge = (category) => {
    const colors = {
      'A': 'bg-green-100 text-green-800',
      'B': 'bg-blue-100 text-blue-800',
      'E-Pass': 'bg-purple-100 text-purple-800'
    }
    return colors[category] || 'bg-gray-100 text-gray-800'
  }

  return (
    <div className="bg-white rounded-xl shadow-lg hover:shadow-xl transition-shadow p-6 border border-gray-100">
      {/* Header */}
      <div className="flex justify-between items-start mb-4">
        <div className="flex-1">
          <div className="flex items-center gap-2 mb-2">
            <span className={`px-3 py-1 rounded-full text-xs font-semibold ${getCategoryBadge(service.category)}`}>
              Category {service.category}
            </span>
            <span className="px-3 py-1 rounded-full text-xs font-semibold bg-gray-100 text-gray-700">
              #{service.priority_rank}
            </span>
          </div>
          <h3 className="text-xl font-bold text-gray-900 mb-1">{service.name.en}</h3>
          <p className="text-gray-600 text-sm">{service.name.te}</p>
        </div>
        <div className="text-right">
          <div className="flex items-center gap-1 text-telangana-primary font-bold text-2xl">
            <IndianRupee className="w-5 h-5" />
            {service.fee}
          </div>
        </div>
      </div>

      {/* Description */}
      <p className="text-gray-700 mb-4 leading-relaxed">{service.description_simple.en}</p>

      {/* Info Grid */}
      <div className="grid grid-cols-2 gap-4 mb-4">
        <div className="flex items-start gap-2">
          <Building2 className="w-5 h-5 text-gray-400 mt-0.5 flex-shrink-0" />
          <div>
            <p className="text-xs text-gray-500">Department</p>
            <p className="font-semibold text-gray-800">{service.department}</p>
          </div>
        </div>
        <div className="flex items-start gap-2">
          <Clock className="w-5 h-5 text-gray-400 mt-0.5 flex-shrink-0" />
          <div>
            <p className="text-xs text-gray-500">Processing Time</p>
            <p className="font-semibold text-gray-800">{service.processing_time}</p>
          </div>
        </div>
      </div>

      {/* Readiness Card - Submission Modes */}
      <div className="bg-gradient-to-r from-blue-50 to-orange-50 rounded-lg p-4 mb-4">
        <h4 className="font-semibold text-gray-800 mb-3 flex items-center gap-2">
          <Globe className="w-4 h-4" />
          Submission Options
        </h4>
        <div className="grid grid-cols-2 gap-3">
          {/* Online Submission */}
          <div className={`p-3 rounded-lg ${service.submission_modes.online.available ? 'bg-green-50 border border-green-200' : 'bg-gray-50 border border-gray-200'}`}>
            <p className="font-medium text-sm mb-1">
              {service.submission_modes.online.available ? '✅ Online' : '❌ Online'}
            </p>
            {service.submission_modes.online.available && (
              <p className="text-xs text-gray-600">Digital submission available</p>
            )}
          </div>

          {/* MeeSeva Center */}
          <div className={`p-3 rounded-lg ${service.submission_modes.meeseva_center.available ? 'bg-green-50 border border-green-200' : 'bg-gray-50 border border-gray-200'}`}>
            <p className="font-medium text-sm mb-1">
              {service.submission_modes.meeseva_center.available ? '✅ MeeSeva' : '❌ MeeSeva'}
            </p>
            {service.submission_modes.meeseva_center.available && service.submission_modes.meeseva_center.requires_stamp && (
              <p className="text-xs text-orange-600 font-semibold">⚠️ ₹2 Court Stamp required</p>
            )}
          </div>
        </div>
      </div>

      {/* Revenue Service Alert */}
      {service.is_revenue && service.submission_modes.meeseva_center.requires_stamp && (
        <div className="bg-orange-50 border border-orange-200 rounded-lg p-3 mb-4 flex items-start gap-2">
          <AlertCircle className="w-5 h-5 text-orange-600 flex-shrink-0 mt-0.5" />
          <div>
            <p className="text-sm font-semibold text-orange-800">Revenue Service Notice</p>
            <p className="text-xs text-orange-700 mt-1">
              This is a Revenue Department service. When submitting at MeeSeva Center, you must bring a ₹2 Court Fee Stamp.
            </p>
          </div>
        </div>
      )}

      {/* Required Documents */}
      <div className="border-t border-gray-200 pt-4">
        <h4 className="font-semibold text-gray-800 mb-2 flex items-center gap-2">
          <FileText className="w-4 h-4" />
          Required Documents ({service.required_documents.length})
        </h4>
        <ul className="space-y-1">
          {service.required_documents.slice(0, 3).map((doc, idx) => (
            <li key={idx} className="text-sm text-gray-700 flex items-start gap-2">
              <span className="text-telangana-primary mt-1">•</span>
              <span>{doc.name.en} {doc.mandatory && <span className="text-red-500">*</span>}</span>
            </li>
          ))}
          {service.required_documents.length > 3 && (
            <li className="text-sm text-gray-500 italic">
              + {service.required_documents.length - 3} more documents
            </li>
          )}
        </ul>
      </div>

      {/* Action Button */}
      {service.submission_modes.online.available && (
        <div className="mt-4 pt-4 border-t border-gray-200">
          <a
            href={service.submission_modes.online.portal_url}
            target="_blank"
            rel="noopener noreferrer"
            className="block w-full bg-telangana-primary hover:bg-telangana-accent text-white font-semibold py-3 px-4 rounded-lg text-center transition-colors"
          >
            Apply Online →
          </a>
        </div>
      )}
    </div>
  )
}

// Made with Bob
